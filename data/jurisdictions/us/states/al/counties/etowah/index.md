---
type: Jurisdiction
title: "Etowah County, AL"
classification: county
fips: "01055"
state: "AL"
demographics:
  population: 103105
  population_under_18: 22582
  population_18_64: 60183
  population_65_plus: 20340
  median_household_income: 54563
  poverty_rate: 16.94
  homeownership_rate: 73.91
  unemployment_rate: 5.9
  median_home_value: 167100
  gini_index: 0.4619
  vacancy_rate: 17.21
  race_white: 79440
  race_black: 15231
  race_asian: 680
  race_native: 526
  hispanic: 5393
  bachelors_plus: 18125
districts:
  - to: "us/states/al/districts/03"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/al/districts/senate/10"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/al/districts/house/29"
    rel: in-district
    area_weight: 0.4656
  - to: "us/states/al/districts/house/30"
    rel: in-district
    area_weight: 0.3168
  - to: "us/states/al/districts/house/28"
    rel: in-district
    area_weight: 0.2174
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Etowah County, AL

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 103105 |
| Under 18 | 22582 |
| 18–64 | 60183 |
| 65+ | 20340 |
| Median household income | 54563 |
| Poverty rate | 16.94 |
| Homeownership rate | 73.91 |
| Unemployment rate | 5.9 |
| Median home value | 167100 |
| Gini index | 0.4619 |
| Vacancy rate | 17.21 |
| White | 79440 |
| Black | 15231 |
| Asian | 680 |
| Native | 526 |
| Hispanic/Latino | 5393 |
| Bachelor's or higher | 18125 |

## Districts

- [AL-03](/us/states/al/districts/03.md) — 100% (congressional)
- [AL Senate District 10](/us/states/al/districts/senate/10.md) — 100% (state senate)
- [AL House District 29](/us/states/al/districts/house/29.md) — 47% (state house)
- [AL House District 30](/us/states/al/districts/house/30.md) — 32% (state house)
- [AL House District 28](/us/states/al/districts/house/28.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
