---
type: Jurisdiction
title: "Vermilion Parish, LA"
classification: county
fips: "22113"
state: "LA"
demographics:
  population: 57123
  population_under_18: 14409
  population_18_64: 33207
  population_65_plus: 9507
  median_household_income: 55707
  poverty_rate: 20.16
  homeownership_rate: 73.36
  unemployment_rate: 5.17
  median_home_value: 163300
  gini_index: 0.466
  vacancy_rate: 16.62
  race_white: 44444
  race_black: 7352
  race_asian: 1128
  race_native: 65
  hispanic: 2574
  bachelors_plus: 8194
districts:
  - to: "us/states/la/districts/03"
    rel: in-district
    area_weight: 0.8466
  - to: "us/states/la/districts/senate/26"
    rel: in-district
    area_weight: 0.8452
  - to: "us/states/la/districts/house/47"
    rel: in-district
    area_weight: 0.7446
  - to: "us/states/la/districts/house/49"
    rel: in-district
    area_weight: 0.0734
  - to: "us/states/la/districts/house/31"
    rel: in-district
    area_weight: 0.0272
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Vermilion Parish, LA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 57123 |
| Under 18 | 14409 |
| 18–64 | 33207 |
| 65+ | 9507 |
| Median household income | 55707 |
| Poverty rate | 20.16 |
| Homeownership rate | 73.36 |
| Unemployment rate | 5.17 |
| Median home value | 163300 |
| Gini index | 0.466 |
| Vacancy rate | 16.62 |
| White | 44444 |
| Black | 7352 |
| Asian | 1128 |
| Native | 65 |
| Hispanic/Latino | 2574 |
| Bachelor's or higher | 8194 |

## Districts

- [LA-03](/us/states/la/districts/03.md) — 85% (congressional)
- [LA Senate District 26](/us/states/la/districts/senate/26.md) — 85% (state senate)
- [LA House District 47](/us/states/la/districts/house/47.md) — 74% (state house)
- [LA House District 49](/us/states/la/districts/house/49.md) — 7% (state house)
- [LA House District 31](/us/states/la/districts/house/31.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
