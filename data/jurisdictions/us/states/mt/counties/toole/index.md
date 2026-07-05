---
type: Jurisdiction
title: "Toole County, MT"
classification: county
fips: "30101"
state: "MT"
demographics:
  population: 5061
  population_under_18: 1066
  population_18_64: 3083
  population_65_plus: 912
  median_household_income: 57731
  poverty_rate: 12.57
  homeownership_rate: 63.12
  unemployment_rate: 4.88
  median_home_value: 218400
  gini_index: 0.4445
  vacancy_rate: 20.24
  race_white: 4221
  race_black: 85
  race_asian: 67
  race_native: 301
  hispanic: 225
  bachelors_plus: 1113
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/mt/districts/senate/9"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/house/18"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Toole County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5061 |
| Under 18 | 1066 |
| 18–64 | 3083 |
| 65+ | 912 |
| Median household income | 57731 |
| Poverty rate | 12.57 |
| Homeownership rate | 63.12 |
| Unemployment rate | 4.88 |
| Median home value | 218400 |
| Gini index | 0.4445 |
| Vacancy rate | 20.24 |
| White | 4221 |
| Black | 85 |
| Asian | 67 |
| Native | 301 |
| Hispanic/Latino | 225 |
| Bachelor's or higher | 1113 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 9](/us/states/mt/districts/senate/9.md) — 100% (state senate)
- [MT House District 18](/us/states/mt/districts/house/18.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
