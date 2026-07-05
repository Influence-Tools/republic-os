---
type: Jurisdiction
title: "Wayne County, NY"
classification: county
fips: "36117"
state: "NY"
demographics:
  population: 90929
  population_under_18: 19083
  population_18_64: 52914
  population_65_plus: 18932
  median_household_income: 74506
  poverty_rate: 11.43
  homeownership_rate: 79.88
  unemployment_rate: 3.32
  median_home_value: 170000
  gini_index: 0.4111
  vacancy_rate: 9.79
  race_white: 79642
  race_black: 2100
  race_asian: 692
  race_native: 233
  hispanic: 4794
  bachelors_plus: 23459
districts:
  - to: "us/states/ny/districts/24"
    rel: in-district
    area_weight: 0.4397
  - to: "us/states/ny/districts/senate/54"
    rel: in-district
    area_weight: 0.4413
  - to: "us/states/ny/districts/house/130"
    rel: in-district
    area_weight: 0.4413
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Wayne County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 90929 |
| Under 18 | 19083 |
| 18–64 | 52914 |
| 65+ | 18932 |
| Median household income | 74506 |
| Poverty rate | 11.43 |
| Homeownership rate | 79.88 |
| Unemployment rate | 3.32 |
| Median home value | 170000 |
| Gini index | 0.4111 |
| Vacancy rate | 9.79 |
| White | 79642 |
| Black | 2100 |
| Asian | 692 |
| Native | 233 |
| Hispanic/Latino | 4794 |
| Bachelor's or higher | 23459 |

## Districts

- [NY-24](/us/states/ny/districts/24.md) — 44% (congressional)
- [NY Senate District 54](/us/states/ny/districts/senate/54.md) — 44% (state senate)
- [NY House District 130](/us/states/ny/districts/house/130.md) — 44% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
