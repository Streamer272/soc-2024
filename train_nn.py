import numpy as np
import torch
import torch.nn as nn
import argparse
from torch.utils.data import random_split, DataLoader, TensorDataset
from torch.optim.lr_scheduler import ReduceLROnPlateau
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(
    prog="train_nn"
)
parser.add_argument("-g", "--graph", action="store_true", default=False, help="Graph losses")
args = parser.parse_args()
graph = args.graph


class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()

        self.features = nn.Sequential(
            nn.Linear(8, 512),
            nn.ReLU(),
            nn.BatchNorm1d(512),
            nn.Dropout(p=0.4),

            nn.Linear(512, 256),
            nn.ReLU(),
            nn.BatchNorm1d(256),
            nn.Dropout(p=0.4),

            nn.Linear(256, 128),
            nn.ReLU(),
            nn.BatchNorm1d(128),
            nn.Dropout(p=0.4),

            nn.Linear(128, 64),
            nn.ReLU(),
            nn.BatchNorm1d(64),
            nn.Dropout(p=0.4),

            nn.Linear(64, 4)
        )

    def forward(self, x):
        return self.features(x)


data = np.load("clean.npy")
data_x = np.append(data[:, 0:2], data[:, 6:12], axis=1)  # grade, sex, ses, occupation, living, commute, sleep, absence
data_y = data[:, 2:6]  # gpa, math, slovak, english
print(f"Loaded data of shape {data.shape}")
print(f"\tx: {data_x.shape}")
print(f"\ty: {data_y.shape}")
print("")

train_size = int(len(data) * 0.8)
test_size = len(data) - train_size
torch.manual_seed(42)

batch_size = 32
epochs = 200
lr = 0.001
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

dataset = TensorDataset(torch.Tensor(data_x), torch.Tensor(data_y))
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])
train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

print(f"Initialized dataloaders")
print(f"\ttrain: {len(train_dataloader)} batches ({len(train_dataset)} samples)")
print(f"\ttest: {len(test_dataloader)} batches ({len(test_dataset)} samples)")
print("")

model = NeuralNetwork()
model.to(device)

print(f"Initialized model")
print(model)
print("")

loss_fn = nn.MSELoss()
optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-5)
scheduler = ReduceLROnPlateau(optimizer, mode='min', patience=5, factor=0.5)

train_losses = []
test_losses = []

for epoch in range(epochs):
    print(f"Epoch {epoch + 1}/{epochs}...\r", end="")

    model.train()
    train_loss = 0.0

    for X, y in train_dataloader:
        X, y = X.to(device), y.to(device)
        optimizer.zero_grad()

        pred = model(X)
        loss = loss_fn(pred, y)

        loss.backward()
        optimizer.step()

        train_loss += loss.item() * X.size(0)

    train_loss /= len(train_dataset)
    train_losses.append(train_loss)

    model.eval()
    test_loss = 0.0

    with torch.no_grad():
        for X, y in test_dataloader:
            X, y = X.to(device), y.to(device)

            pred = model(X)
            loss = loss_fn(pred, y)

            test_loss = loss.item() * X.size(0)

    test_loss /= len(test_dataset)
    test_losses.append(test_loss)

    print(
        f"Epoch {epoch + 1}/{epochs}\n"
        f"Train loss: {train_loss:.4f}\n"
        f"Test loss: {test_loss:.4f}\n"
    )
    scheduler.step(test_loss)

print(f"Average train loss: {sum(train_losses) / len(train_losses):.4f}")
print(f"Average test loss: {sum(test_losses) / len(test_losses):.4f}")

torch.save(model.state_dict(), "model.pth")
print("Model saved to model.pth")

model.eval()
all_preds = []
all_labels = []

with torch.no_grad():
    for X, y in test_dataloader:
        X, y = X.to(device), y.to(device)
        pred = model(X)
        all_preds.append(pred.argmax(dim=1).cpu().numpy())
        all_labels.append(y.argmax(dim=1).cpu().numpy())

all_preds = np.concatenate(all_preds)
all_labels = np.concatenate(all_labels)

accuracy = accuracy_score(all_labels, all_preds)
precision = precision_score(all_labels, all_preds, average='weighted', zero_division=0)
recall = recall_score(all_labels, all_preds, average='weighted', zero_division=0)
f1 = f1_score(all_labels, all_preds, average='weighted')

print("\nEvaluation Metrics:")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1 Score:  {f1:.4f}")

if graph:
    x = np.arange(1, epochs + 1, 1)

    plt.figure(figsize=(8, 6))
    plt.plot(x, train_losses, color="red", label="Strata trénovania")
    plt.plot(x, test_losses, color="blue", label="Strata testovania")

    plt.xlabel("Epocha")
    plt.ylabel("Strata")
    plt.title("Priebeh trénovania")

    plt.text(0.99, 0.99,
             f"Presnosť: {accuracy:.4f}\nPrecíznosť: {precision:.4f}\nOdvolanie: {recall:.4f}\nF1 skóre: {f1:.4f}",
             ha="right", va="top", transform=plt.gca().transAxes, fontweight="bold")

    plt.legend()
    plt.tight_layout()
    plt.show()
