---
type: Jurisdiction
title: "Tallapoosa County, AL"
classification: county
fips: "01123"
state: "AL"
demographics:
  population: 40938
  population_under_18: 9108
  population_18_64: 11085
  population_65_plus: 20745
  median_household_income: 59356
  poverty_rate: 16.32
  homeownership_rate: 76.07
  unemployment_rate: 4.94
  median_home_value: 158500
  gini_index: 0.4767
  vacancy_rate: 26.27
  race_white: 27854
  race_black: 9587
  race_asian: 260
  race_native: 102
  hispanic: 1183
  bachelors_plus: 8176
districts:
  - to: "us/states/al/districts/03"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/al/districts/senate/27"
    rel: in-district
    area_weight: 0.8512
  - to: "us/states/al/districts/senate/30"
    rel: in-district
    area_weight: 0.1486
  - to: "us/states/al/districts/house/81"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Tallapoosa County, AL

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 40938 |
| Under 18 | 9108 |
| 18–64 | 11085 |
| 65+ | 20745 |
| Median household income | 59356 |
| Poverty rate | 16.32 |
| Homeownership rate | 76.07 |
| Unemployment rate | 4.94 |
| Median home value | 158500 |
| Gini index | 0.4767 |
| Vacancy rate | 26.27 |
| White | 27854 |
| Black | 9587 |
| Asian | 260 |
| Native | 102 |
| Hispanic/Latino | 1183 |
| Bachelor's or higher | 8176 |

## Districts

- [AL-03](/us/states/al/districts/03.md) — 100% (congressional)
- [AL Senate District 27](/us/states/al/districts/senate/27.md) — 85% (state senate)
- [AL Senate District 30](/us/states/al/districts/senate/30.md) — 15% (state senate)
- [AL House District 81](/us/states/al/districts/house/81.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
