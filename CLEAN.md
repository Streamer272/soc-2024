# Clean dataset

The cleaned dataset will have the following structure:

| Index | Name       | Type  | Range |
|-------|------------|-------|-------|
| 0     | Grade      | int   | [1-5] |
| 1     | Sex        | enum  | [0-1] |
| 2     | GPA        | float | [1-5] |
| 3     | Math       | int   | [1-5] |
| 4     | Slovak     | int   | [1-5] |
| 5     | English    | int   | [1-5] |
| 6     | Occupation | enum  | [0-5] |
| 7     | Living     | enum  | [0-4] |
| 8     | Commute    | enum  | [0-4] |
| 9     | Absence    | int   | -     |

### Sex

```
0 - zena
1 - muz
```

### Occupation

```
0 - work hours / week >= 10
1 - work hours / week < 10
2 - sport
3 - music
4 - other
5 - none
```

### Living

```
0 - with family
1 - with family member
2 - alone / roomates
3 - dorms
4 - other
```

### Commute

```
0 - dorms
1 - <= 15m
2 - <= 30m
3 - <= 1h
4 - > 1h
```
