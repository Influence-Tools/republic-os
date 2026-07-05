---
type: Jurisdiction
title: "Petersburg Borough, AK"
classification: county
fips: "02195"
state: "AK"
demographics:
  population: 3409
  population_under_18: 720
  population_18_64: 962
  population_65_plus: 1727
  median_household_income: 75125
  poverty_rate: 6.97
  homeownership_rate: 65.72
  unemployment_rate: 3.77
  median_home_value: 315100
  gini_index: 0.3826
  vacancy_rate: 26.41
  race_white: 2160
  race_black: 45
  race_asian: 424
  race_native: 261
  hispanic: 371
  bachelors_plus: 849
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.8046
  - to: "us/states/ak/districts/senate/a"
    rel: in-district
    area_weight: 0.8001
  - to: "us/states/ak/districts/house/2"
    rel: in-district
    area_weight: 0.8001
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Petersburg Borough, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3409 |
| Under 18 | 720 |
| 18–64 | 962 |
| 65+ | 1727 |
| Median household income | 75125 |
| Poverty rate | 6.97 |
| Homeownership rate | 65.72 |
| Unemployment rate | 3.77 |
| Median home value | 315100 |
| Gini index | 0.3826 |
| Vacancy rate | 26.41 |
| White | 2160 |
| Black | 45 |
| Asian | 424 |
| Native | 261 |
| Hispanic/Latino | 371 |
| Bachelor's or higher | 849 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 80% (congressional)
- [AK Senate District A](/us/states/ak/districts/senate/a.md) — 80% (state senate)
- [AK House District 2](/us/states/ak/districts/house/2.md) — 80% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
