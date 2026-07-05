---
type: Jurisdiction
title: "Giles County, TN"
classification: county
fips: "47055"
state: "TN"
demographics:
  population: 30620
  population_under_18: 6318
  population_18_64: 17839
  population_65_plus: 6463
  median_household_income: 62307
  poverty_rate: 12.79
  homeownership_rate: 73.3
  unemployment_rate: 4.4
  median_home_value: 234300
  gini_index: 0.4666
  vacancy_rate: 15.21
  race_white: 25546
  race_black: 2617
  race_asian: 150
  race_native: 60
  hispanic: 894
  bachelors_plus: 5848
districts:
  - to: "us/states/tn/districts/04"
    rel: in-district
    area_weight: 0.9966
  - to: "us/states/tn/districts/senate/28"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/house/70"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Giles County, TN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30620 |
| Under 18 | 6318 |
| 18–64 | 17839 |
| 65+ | 6463 |
| Median household income | 62307 |
| Poverty rate | 12.79 |
| Homeownership rate | 73.3 |
| Unemployment rate | 4.4 |
| Median home value | 234300 |
| Gini index | 0.4666 |
| Vacancy rate | 15.21 |
| White | 25546 |
| Black | 2617 |
| Asian | 150 |
| Native | 60 |
| Hispanic/Latino | 894 |
| Bachelor's or higher | 5848 |

## Districts

- [TN-04](/us/states/tn/districts/04.md) — 100% (congressional)
- [TN Senate District 28](/us/states/tn/districts/senate/28.md) — 100% (state senate)
- [TN House District 70](/us/states/tn/districts/house/70.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
