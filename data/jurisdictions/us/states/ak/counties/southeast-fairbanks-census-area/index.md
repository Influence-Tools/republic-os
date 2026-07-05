---
type: Jurisdiction
title: "Southeast Fairbanks Census Area, AK"
classification: county
fips: "02240"
state: "AK"
demographics:
  population: 7068
  population_under_18: 1861
  population_18_64: 2294
  population_65_plus: 2913
  median_household_income: 73882
  poverty_rate: 12.7
  homeownership_rate: 74.69
  unemployment_rate: 6.47
  median_home_value: 282000
  gini_index: 0.4364
  vacancy_rate: 28.96
  race_white: 5243
  race_black: 57
  race_asian: 120
  race_native: 647
  hispanic: 421
  bachelors_plus: 1453
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ak/districts/senate/r"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ak/districts/house/36"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Southeast Fairbanks Census Area, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7068 |
| Under 18 | 1861 |
| 18–64 | 2294 |
| 65+ | 2913 |
| Median household income | 73882 |
| Poverty rate | 12.7 |
| Homeownership rate | 74.69 |
| Unemployment rate | 6.47 |
| Median home value | 282000 |
| Gini index | 0.4364 |
| Vacancy rate | 28.96 |
| White | 5243 |
| Black | 57 |
| Asian | 120 |
| Native | 647 |
| Hispanic/Latino | 421 |
| Bachelor's or higher | 1453 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 100% (congressional)
- [AK Senate District R](/us/states/ak/districts/senate/r.md) — 100% (state senate)
- [AK House District 36](/us/states/ak/districts/house/36.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
