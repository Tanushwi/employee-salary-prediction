import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# Step 1: Load dataset
df = pd.read_csv('employee_data.csv')

# Step 2: Preprocess
df = pd.get_dummies(df, drop_first=True)  # Encode categorical variables

# Step 3: Split into X (features) and y (target)
X = df.drop('Salary', axis=1)
y = df['Salary']

# Step 4: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Predict and evaluate
y_pred = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
