---
type: Jurisdiction
title: "Yakutat City and Borough, AK"
classification: county
fips: "02282"
state: "AK"
demographics:
  population: 527
  population_under_18: 67
  population_18_64: 204
  population_65_plus: 256
  median_household_income: 85000
  poverty_rate: 11.88
  homeownership_rate: 56.31
  unemployment_rate: 0.9
  median_home_value: 219400
  gini_index: 0.3579
  vacancy_rate: 48.24
  race_white: 133
  race_black: 25
  race_asian: 93
  race_native: 111
  hispanic: 46
  bachelors_plus: 84
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.869
  - to: "us/states/ak/districts/senate/a"
    rel: in-district
    area_weight: 0.8669
  - to: "us/states/ak/districts/house/2"
    rel: in-district
    area_weight: 0.8669
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Yakutat City and Borough, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 527 |
| Under 18 | 67 |
| 18–64 | 204 |
| 65+ | 256 |
| Median household income | 85000 |
| Poverty rate | 11.88 |
| Homeownership rate | 56.31 |
| Unemployment rate | 0.9 |
| Median home value | 219400 |
| Gini index | 0.3579 |
| Vacancy rate | 48.24 |
| White | 133 |
| Black | 25 |
| Asian | 93 |
| Native | 111 |
| Hispanic/Latino | 46 |
| Bachelor's or higher | 84 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 87% (congressional)
- [AK Senate District A](/us/states/ak/districts/senate/a.md) — 87% (state senate)
- [AK House District 2](/us/states/ak/districts/house/2.md) — 87% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
