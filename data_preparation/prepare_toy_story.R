setwd("/Users/juanmalagon/Desktop/Malagon-Haelermans/ftpdbicfes/4. Saber11/4. Clasificación de Planteles")

require(ggplot2)
require(dplyr)

readLines(textConnection("¬",encoding="UTF-8"))

##################################
# 2018
sb11.20182 <- read.table(text = gsub("¬", "\t", readLines('SB11-CLASIFI-PLANTELES-20182.txt')), 
                 header = TRUE, 
                 sep = "\t",
                 fileEncoding = 'UTF-8',
                 quote = "",
                 comment.char = "",
                 strip.white = TRUE,
                 dec = ',')

sb11.20181 <- read.table('SB11-CLASIFI-PLANTELES-20181.txt', 
                         header = TRUE, 
                         sep='|',
                         fileEncoding = 'latin1',
                         quote = "",
                         comment.char = "",
                         strip.white = TRUE,
                         dec = '.')

sb11.2018 <- rbind(sb11.20181, sb11.20182)

remove(sb11.20181)
remove(sb11.20182)

summary(sb11.2018)

setwd("/Users/juanmalagon/Desktop/Malagon-Haelermans/dane/educacion_formal_2018")

computing <- read.csv('Tenencia y numero de equipos de computo por sede educativa.csv',
                                              header = TRUE, 
                                              sep=';',
                                              encoding = 'UTF-8')

##################################
# Visualizations

ggplot(sb11.2018, 
       aes(INDICE_TOTAL)) + 
  geom_density(alpha = 0.2)

ggplot(sb11.2018, 
       aes(INDICE_TOTAL, 
           fill = COLE_NATURALEZA)) + 
  geom_histogram(alpha=0.2, bins = 100)

ggplot(sb11.2018, 
       aes(INDICE_TOTAL, 
           fill = COLE_NATURALEZA)) + 
  geom_density(alpha=0.2)

ggplot(sb11.2018, 
       aes(INDICE_TOTAL, 
           fill = COLE_DEPTO_COLEGIO)) + 
  geom_density(alpha=0.2)

depts <- sb11.2018 %>%
  group_by(COLE_DEPTO_COLEGIO) %>%
  summarise(MEAN_BY_DEPT = mean(INDICE_TOTAL),
            MEDIAN_BY_DEPT = median(INDICE_TOTAL))

temp <- sb11.2018 %>%
  group_by(COLE_DEPTO_COLEGIO) %>%
  mutate(MEAN_BY_DEPT = mean(INDICE_TOTAL)) %>%
  ungroup()

ggplot(temp[temp$MEAN_BY_DEPT>median(temp$INDICE_TOTAL),], 
       aes(INDICE_TOTAL, 
           fill = COLE_DEPTO_COLEGIO)) + 
  geom_density(alpha=0.2)

##################################


