import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

# ---------------------------------------------------
# 1. Pairplot of numeric variables in 'tips'
# ---------------------------------------------------
tips = sns.load_dataset("tips")
sns.pairplot(tips[["total_bill", "tip", "size"]], corner=False)
plt.suptitle("Tips Dataset: Pairwise Relationships", y=1.02)
plt.show()


# ---------------------------------------------------
# 2. Heatmap of passengers (months x years) from 'flights'
# ---------------------------------------------------
flights = sns.load_dataset("flights")
flights_pivot = flights.pivot_table(index="month", columns="year", values="passengers")

plt.figure(figsize=(10, 6))
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Number of Passengers by Month and Year")
plt.xlabel("Year")
plt.ylabel("Month")
plt.show()


# ---------------------------------------------------
# 3. Relplot: fMRI signal over time by event type
# ---------------------------------------------------
fmri = sns.load_dataset("fmri")
sns.relplot(data=fmri, x="timepoint", y="signal", hue="event", kind="line", height=5, aspect=1.4)
plt.title("fMRI Signal Over Time by Event Type")
plt.show()


# ---------------------------------------------------
# 4. Catplot: survival rate by class with confidence intervals
# ---------------------------------------------------
titanic = sns.load_dataset("titanic")
g = sns.catplot(data=titanic, x="class", y="survived", kind="bar",
                errorbar=("ci", 95), hue="class", palette="Set2", height=5, aspect=1.2)
g.set_axis_labels("Passenger Class", "Survival Rate")
g.figure.suptitle("Titanic Survival Rate by Class (95% CI)", y=1.02)
plt.show()


# ---------------------------------------------------
# 5. Jointplot with regression line: penguins
# ---------------------------------------------------
penguins = sns.load_dataset("penguins").dropna(subset=["bill_length_mm", "flipper_length_mm"])
sns.jointplot(data=penguins, x="bill_length_mm", y="flipper_length_mm", kind="reg", color="teal")
plt.suptitle("Bill Length vs Flipper Length", y=1.02)
plt.show()