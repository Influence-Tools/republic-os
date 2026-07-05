---
type: Jurisdiction
title: "Custer County, MT"
classification: county
fips: "30017"
state: "MT"
demographics:
  population: 11961
  population_under_18: 2369
  population_18_64: 7110
  population_65_plus: 2482
  median_household_income: 70605
  poverty_rate: 11.34
  homeownership_rate: 69.87
  unemployment_rate: 3.44
  median_home_value: 219100
  gini_index: 0.4246
  vacancy_rate: 12.9
  race_white: 10817
  race_black: 4
  race_asian: 54
  race_native: 220
  hispanic: 409
  bachelors_plus: 2918
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/17"
    rel: in-district
    area_weight: 0.778
  - to: "us/states/mt/districts/senate/18"
    rel: in-district
    area_weight: 0.222
  - to: "us/states/mt/districts/house/34"
    rel: in-district
    area_weight: 0.778
  - to: "us/states/mt/districts/house/36"
    rel: in-district
    area_weight: 0.222
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Custer County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11961 |
| Under 18 | 2369 |
| 18–64 | 7110 |
| 65+ | 2482 |
| Median household income | 70605 |
| Poverty rate | 11.34 |
| Homeownership rate | 69.87 |
| Unemployment rate | 3.44 |
| Median home value | 219100 |
| Gini index | 0.4246 |
| Vacancy rate | 12.9 |
| White | 10817 |
| Black | 4 |
| Asian | 54 |
| Native | 220 |
| Hispanic/Latino | 409 |
| Bachelor's or higher | 2918 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 17](/us/states/mt/districts/senate/17.md) — 78% (state senate)
- [MT Senate District 18](/us/states/mt/districts/senate/18.md) — 22% (state senate)
- [MT House District 34](/us/states/mt/districts/house/34.md) — 78% (state house)
- [MT House District 36](/us/states/mt/districts/house/36.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
