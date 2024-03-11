library(dplyr)
library(factoextra)
library(ggplot2)
library(readxl)
library(clusterSim)
library(MASS)

# Loading data 
data <- read_excel("data.xlsx")
data <- data.frame(data) 
df <- subset(data, select = -country)
rownames(df) <- names

# Data normalization
data_normalized <- scale(df)

# Correlation matrix
corr_matrix <- cor(data_normalized)
ggcorrplot(corr_matrix)
cortest.bartlett(corr_matrix)

# Boxplots for variables
pl1 <- ggplot(data = data, aes(x = 0, y = life_expectancy)) +
  geom_boxplot(fill = "lightblue", width = 0.5) +
  geom_jitter(color = "navyblue") +
  theme_bw()

pl2 <- ggplot(data = data, aes(x = 0, y = gdp_per_capita)) +
  geom_boxplot(fill = "lightblue", width = 0.5) +
  geom_jitter(color = "navyblue") +
  theme_bw()

pl3 <- ggplot(data = data, aes(x = 0, y = unemployment_rate)) +
  geom_boxplot(fill = "lightblue", width = 0.5) +
  geom_jitter(color = "navyblue") +
  theme_bw()

pl4 <- ggplot(data = data, aes(x = 0, y = crime_index)) +
  geom_boxplot(fill = "lightblue", width = 0.5) +
  geom_jitter(color = "navyblue") +
  theme_bw()

pl5 <- ggplot(data = data, aes(x = 0, y = air_quality_index)) +
  geom_boxplot(fill = "lightblue", width = 0.5) +
  geom_jitter(color = "navyblue") +
  theme_bw()

pl6 <- ggplot(data = data, aes(x = 0, y = gini_index)) +
  geom_boxplot(fill = "lightblue", width = 0.5) +
  geom_jitter(color = "navyblue") +
  theme_bw()

ggarrange(pl1, pl2, pl3, pl4, pl5, pl6, ncol = 6, nrow = 1)

# Cluster analysis - k-means method
data_km <- data.frame(data_km)
names <- data_km$country
df <- subset(data_km, select = -country)
rownames(df) <- names

#Standardization
df <- scale(df)

# Removing outliers
df_1 <- df[rownames(df) != "India", ]
df_1 <- df_1[rownames(df_1) != "South Africa", ]

# Elbow method
fviz_nbclust(df, pam, method = "wss")

# K-means clustering
set.seed(3)
kmed <- pam(df_1, k = 3)
fviz_cluster(kmed, data = df)

# Cluster analysis - hierarchical clustering using Ward's method
df <- scale(df)

# Distance
distEuclidean <- dist(df_1, method = "euclidean")

wardEuclidean <- hclust(distEuclidean, method = "ward.D2")

dend_data <- dendro_data(wardEuclidean, type = "rectangle")

dend_ward_euclidean <- color_branches(wardEuclidean, k = 2)
plot(dend_ward_euclidean)