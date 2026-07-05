---
type: Jurisdiction
title: "Bethel Census Area, AK"
classification: county
fips: "02050"
state: "AK"
demographics:
  population: 18394
  population_under_18: 6944
  population_18_64: 6234
  population_65_plus: 5216
  median_household_income: 73996
  poverty_rate: 25.61
  homeownership_rate: 61.56
  unemployment_rate: 15.94
  median_home_value: 168100
  gini_index: 0.4476
  vacancy_rate: 19.68
  race_white: 1529
  race_black: 228
  race_asian: 289
  race_native: 15445
  hispanic: 270
  bachelors_plus: 1792
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.9342
  - to: "us/states/ak/districts/senate/s"
    rel: in-district
    area_weight: 0.9336
  - to: "us/states/ak/districts/house/38"
    rel: in-district
    area_weight: 0.4786
  - to: "us/states/ak/districts/house/37"
    rel: in-district
    area_weight: 0.455
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Bethel Census Area, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18394 |
| Under 18 | 6944 |
| 18–64 | 6234 |
| 65+ | 5216 |
| Median household income | 73996 |
| Poverty rate | 25.61 |
| Homeownership rate | 61.56 |
| Unemployment rate | 15.94 |
| Median home value | 168100 |
| Gini index | 0.4476 |
| Vacancy rate | 19.68 |
| White | 1529 |
| Black | 228 |
| Asian | 289 |
| Native | 15445 |
| Hispanic/Latino | 270 |
| Bachelor's or higher | 1792 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 93% (congressional)
- [AK Senate District S](/us/states/ak/districts/senate/s.md) — 93% (state senate)
- [AK House District 38](/us/states/ak/districts/house/38.md) — 48% (state house)
- [AK House District 37](/us/states/ak/districts/house/37.md) — 46% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
