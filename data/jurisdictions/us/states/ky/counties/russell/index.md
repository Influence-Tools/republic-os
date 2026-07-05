---
type: Jurisdiction
title: "Russell County, KY"
classification: county
fips: "21207"
state: "KY"
demographics:
  population: 18221
  population_under_18: 4212
  population_18_64: 10261
  population_65_plus: 3748
  median_household_income: 44738
  poverty_rate: 23.11
  homeownership_rate: 70.8
  unemployment_rate: 6.45
  median_home_value: 163200
  gini_index: 0.4959
  vacancy_rate: 25.64
  race_white: 16853
  race_black: 224
  race_asian: 50
  race_native: 3
  hispanic: 842
  bachelors_plus: 2892
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/ky/districts/senate/15"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ky/districts/house/83"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Russell County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18221 |
| Under 18 | 4212 |
| 18–64 | 10261 |
| 65+ | 3748 |
| Median household income | 44738 |
| Poverty rate | 23.11 |
| Homeownership rate | 70.8 |
| Unemployment rate | 6.45 |
| Median home value | 163200 |
| Gini index | 0.4959 |
| Vacancy rate | 25.64 |
| White | 16853 |
| Black | 224 |
| Asian | 50 |
| Native | 3 |
| Hispanic/Latino | 842 |
| Bachelor's or higher | 2892 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 15](/us/states/ky/districts/senate/15.md) — 100% (state senate)
- [KY House District 83](/us/states/ky/districts/house/83.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
