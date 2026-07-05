---
type: Jurisdiction
title: "Dillingham Census Area, AK"
classification: county
fips: "02070"
state: "AK"
demographics:
  population: 4724
  population_under_18: 1582
  population_18_64: 1552
  population_65_plus: 1590
  median_household_income: 78533
  poverty_rate: 19.46
  homeownership_rate: 61.37
  unemployment_rate: 10.54
  median_home_value: 159000
  gini_index: 0.4359
  vacancy_rate: 41.52
  race_white: 725
  race_black: 32
  race_asian: 86
  race_native: 3361
  hispanic: 177
  bachelors_plus: 686
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.9235
  - to: "us/states/ak/districts/senate/s"
    rel: in-district
    area_weight: 0.9213
  - to: "us/states/ak/districts/house/37"
    rel: in-district
    area_weight: 0.9213
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Dillingham Census Area, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4724 |
| Under 18 | 1582 |
| 18–64 | 1552 |
| 65+ | 1590 |
| Median household income | 78533 |
| Poverty rate | 19.46 |
| Homeownership rate | 61.37 |
| Unemployment rate | 10.54 |
| Median home value | 159000 |
| Gini index | 0.4359 |
| Vacancy rate | 41.52 |
| White | 725 |
| Black | 32 |
| Asian | 86 |
| Native | 3361 |
| Hispanic/Latino | 177 |
| Bachelor's or higher | 686 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 92% (congressional)
- [AK Senate District S](/us/states/ak/districts/senate/s.md) — 92% (state senate)
- [AK House District 37](/us/states/ak/districts/house/37.md) — 92% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
