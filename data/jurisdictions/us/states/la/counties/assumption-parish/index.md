---
type: Jurisdiction
title: "Assumption Parish, LA"
classification: county
fips: "22007"
state: "LA"
demographics:
  population: 20484
  population_under_18: 4188
  population_18_64: 12129
  population_65_plus: 4167
  median_household_income: 51423
  poverty_rate: 15.29
  homeownership_rate: 84.81
  unemployment_rate: 4.77
  median_home_value: 150300
  gini_index: 0.4839
  vacancy_rate: 12.28
  race_white: 13317
  race_black: 5664
  race_asian: 186
  race_native: 143
  hispanic: 872
  bachelors_plus: 2669
districts:
  - to: "us/states/la/districts/02"
    rel: in-district
    area_weight: 0.9979
  - to: "us/states/la/districts/senate/2"
    rel: in-district
    area_weight: 0.5089
  - to: "us/states/la/districts/senate/21"
    rel: in-district
    area_weight: 0.4911
  - to: "us/states/la/districts/house/60"
    rel: in-district
    area_weight: 0.7754
  - to: "us/states/la/districts/house/51"
    rel: in-district
    area_weight: 0.2245
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Assumption Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20484 |
| Under 18 | 4188 |
| 18–64 | 12129 |
| 65+ | 4167 |
| Median household income | 51423 |
| Poverty rate | 15.29 |
| Homeownership rate | 84.81 |
| Unemployment rate | 4.77 |
| Median home value | 150300 |
| Gini index | 0.4839 |
| Vacancy rate | 12.28 |
| White | 13317 |
| Black | 5664 |
| Asian | 186 |
| Native | 143 |
| Hispanic/Latino | 872 |
| Bachelor's or higher | 2669 |

## Districts

- [LA-02](/us/states/la/districts/02.md) — 100% (congressional)
- [LA Senate District 2](/us/states/la/districts/senate/2.md) — 51% (state senate)
- [LA Senate District 21](/us/states/la/districts/senate/21.md) — 49% (state senate)
- [LA House District 60](/us/states/la/districts/house/60.md) — 78% (state house)
- [LA House District 51](/us/states/la/districts/house/51.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
