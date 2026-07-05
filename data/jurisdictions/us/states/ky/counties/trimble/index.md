---
type: Jurisdiction
title: "Trimble County, KY"
classification: county
fips: "21223"
state: "KY"
demographics:
  population: 8550
  population_under_18: 1812
  population_18_64: 5152
  population_65_plus: 1586
  median_household_income: 66027
  poverty_rate: 13.28
  homeownership_rate: 79.72
  unemployment_rate: 6.18
  median_home_value: 172000
  gini_index: 0.4679
  vacancy_rate: 12.84
  race_white: 7879
  race_black: 97
  race_asian: 24
  race_native: 9
  hispanic: 254
  bachelors_plus: 1491
districts:
  - to: "us/states/ky/districts/04"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ky/districts/senate/6"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ky/districts/house/47"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Trimble County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8550 |
| Under 18 | 1812 |
| 18–64 | 5152 |
| 65+ | 1586 |
| Median household income | 66027 |
| Poverty rate | 13.28 |
| Homeownership rate | 79.72 |
| Unemployment rate | 6.18 |
| Median home value | 172000 |
| Gini index | 0.4679 |
| Vacancy rate | 12.84 |
| White | 7879 |
| Black | 97 |
| Asian | 24 |
| Native | 9 |
| Hispanic/Latino | 254 |
| Bachelor's or higher | 1491 |

## Districts

- [KY-04](/us/states/ky/districts/04.md) — 100% (congressional)
- [KY Senate District 6](/us/states/ky/districts/senate/6.md) — 100% (state senate)
- [KY House District 47](/us/states/ky/districts/house/47.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
