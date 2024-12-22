import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import random_split, DataLoader, TensorDataset
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()

        self.features = nn.Sequential(
            nn.Linear(8, 256),
            nn.ReLU(),
            nn.Dropout(p=0.2),

            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Dropout(p=0.2),

            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Dropout(p=0.2),

            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Dropout(p=0.2),

            nn.Linear(256, 4),
            nn.ReLU()
        )

        self.lstm = nn.LSTM(input_size=4, hidden_size=64, batch_first=True)
        self.output_layer = nn.Linear(64, 4)

    def forward(self, x):
        x = self.features(x)
        x = x.unsqueeze(1)
        lstm_out, _ = self.lstm(x)
        x = lstm_out.squeeze(1)
        return self.output_layer(x)


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
epochs = 100
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
optimizer = torch.optim.Adam(model.parameters(), lr=lr)

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

    model.eval()
    test_loss = 0.0

    with torch.no_grad():
        for X, y in test_dataloader:
            X, y = X.to(device), y.to(device)

            pred = model(X)
            loss = loss_fn(pred, y)

            test_loss = loss.item() * X.size(0)

    test_loss /= len(test_dataset)

    print(
        f"Epoch {epoch + 1}/{epochs}\n"
        f"Train loss: {train_loss:.4f}\n"
        f"Test loss: {test_loss:.4f}\n"
    )

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
