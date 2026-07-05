---
type: Jurisdiction
title: "Starke County, IN"
classification: county
fips: "18149"
state: "IN"
demographics:
  population: 23365
  population_under_18: 5267
  population_18_64: 13272
  population_65_plus: 4826
  median_household_income: 63960
  poverty_rate: 13.37
  homeownership_rate: 82.97
  unemployment_rate: 3.37
  median_home_value: 157700
  gini_index: 0.3952
  vacancy_rate: 20.31
  race_white: 21565
  race_black: 126
  race_asian: 77
  race_native: 81
  hispanic: 1016
  bachelors_plus: 2687
districts:
  - to: "us/states/in/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/senate/8"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/house/16"
    rel: in-district
    area_weight: 0.6382
  - to: "us/states/in/districts/house/20"
    rel: in-district
    area_weight: 0.3618
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Starke County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23365 |
| Under 18 | 5267 |
| 18–64 | 13272 |
| 65+ | 4826 |
| Median household income | 63960 |
| Poverty rate | 13.37 |
| Homeownership rate | 82.97 |
| Unemployment rate | 3.37 |
| Median home value | 157700 |
| Gini index | 0.3952 |
| Vacancy rate | 20.31 |
| White | 21565 |
| Black | 126 |
| Asian | 77 |
| Native | 81 |
| Hispanic/Latino | 1016 |
| Bachelor's or higher | 2687 |

## Districts

- [IN-02](/us/states/in/districts/02.md) — 100% (congressional)
- [IN Senate District 8](/us/states/in/districts/senate/8.md) — 100% (state senate)
- [IN House District 16](/us/states/in/districts/house/16.md) — 64% (state house)
- [IN House District 20](/us/states/in/districts/house/20.md) — 36% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
