---
type: Jurisdiction
title: "Mecklenburg County, VA"
classification: county
fips: "51117"
state: "VA"
demographics:
  population: 30516
  population_under_18: 5603
  population_18_64: 16697
  population_65_plus: 8216
  median_household_income: 57045
  poverty_rate: 16.34
  homeownership_rate: 68.31
  unemployment_rate: 2.62
  median_home_value: 192600
  gini_index: 0.5066
  vacancy_rate: 29.75
  race_white: 18792
  race_black: 9895
  race_asian: 301
  race_native: 47
  hispanic: 972
  bachelors_plus: 6648
districts:
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/va/districts/senate/9"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/va/districts/house/50"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Mecklenburg County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30516 |
| Under 18 | 5603 |
| 18–64 | 16697 |
| 65+ | 8216 |
| Median household income | 57045 |
| Poverty rate | 16.34 |
| Homeownership rate | 68.31 |
| Unemployment rate | 2.62 |
| Median home value | 192600 |
| Gini index | 0.5066 |
| Vacancy rate | 29.75 |
| White | 18792 |
| Black | 9895 |
| Asian | 301 |
| Native | 47 |
| Hispanic/Latino | 972 |
| Bachelor's or higher | 6648 |

## Districts

- [VA-05](/us/states/va/districts/05.md) — 100% (congressional)
- [VA Senate District 9](/us/states/va/districts/senate/9.md) — 100% (state senate)
- [VA House District 50](/us/states/va/districts/house/50.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
