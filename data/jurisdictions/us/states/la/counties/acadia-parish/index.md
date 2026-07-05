---
type: Jurisdiction
title: "Acadia Parish, LA"
classification: county
fips: "22001"
state: "LA"
demographics:
  population: 56955
  population_under_18: 14789
  population_18_64: 32776
  population_65_plus: 9390
  median_household_income: 45562
  poverty_rate: 24.98
  homeownership_rate: 67.03
  unemployment_rate: 7.72
  median_home_value: 155500
  gini_index: 0.4929
  vacancy_rate: 11.98
  race_white: 43868
  race_black: 9110
  race_asian: 103
  race_native: 31
  hispanic: 1904
  bachelors_plus: 6873
districts:
  - to: "us/states/la/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/la/districts/senate/26"
    rel: in-district
    area_weight: 0.8052
  - to: "us/states/la/districts/senate/25"
    rel: in-district
    area_weight: 0.1948
  - to: "us/states/la/districts/house/42"
    rel: in-district
    area_weight: 0.517
  - to: "us/states/la/districts/house/41"
    rel: in-district
    area_weight: 0.4825
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Acadia Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 56955 |
| Under 18 | 14789 |
| 18–64 | 32776 |
| 65+ | 9390 |
| Median household income | 45562 |
| Poverty rate | 24.98 |
| Homeownership rate | 67.03 |
| Unemployment rate | 7.72 |
| Median home value | 155500 |
| Gini index | 0.4929 |
| Vacancy rate | 11.98 |
| White | 43868 |
| Black | 9110 |
| Asian | 103 |
| Native | 31 |
| Hispanic/Latino | 1904 |
| Bachelor's or higher | 6873 |

## Districts

- [LA-03](/us/states/la/districts/03.md) — 100% (congressional)
- [LA Senate District 26](/us/states/la/districts/senate/26.md) — 81% (state senate)
- [LA Senate District 25](/us/states/la/districts/senate/25.md) — 19% (state senate)
- [LA House District 42](/us/states/la/districts/house/42.md) — 52% (state house)
- [LA House District 41](/us/states/la/districts/house/41.md) — 48% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
