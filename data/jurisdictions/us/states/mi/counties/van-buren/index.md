---
type: Jurisdiction
title: "Van Buren County, MI"
classification: county
fips: "26159"
state: "MI"
demographics:
  population: 75795
  population_under_18: 17385
  population_18_64: 43332
  population_65_plus: 15078
  median_household_income: 68114
  poverty_rate: 14.31
  homeownership_rate: 80.57
  unemployment_rate: 4.17
  median_home_value: 206500
  gini_index: 0.4375
  vacancy_rate: 18.13
  race_white: 60819
  race_black: 2689
  race_asian: 400
  race_native: 592
  hispanic: 9498
  bachelors_plus: 16604
districts:
  - to: "us/states/mi/districts/04"
    rel: in-district
    area_weight: 0.5713
  - to: "us/states/mi/districts/senate/20"
    rel: in-district
    area_weight: 0.5392
  - to: "us/states/mi/districts/senate/19"
    rel: in-district
    area_weight: 0.0321
  - to: "us/states/mi/districts/house/39"
    rel: in-district
    area_weight: 0.52
  - to: "us/states/mi/districts/house/38"
    rel: in-district
    area_weight: 0.0512
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Van Buren County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 75795 |
| Under 18 | 17385 |
| 18–64 | 43332 |
| 65+ | 15078 |
| Median household income | 68114 |
| Poverty rate | 14.31 |
| Homeownership rate | 80.57 |
| Unemployment rate | 4.17 |
| Median home value | 206500 |
| Gini index | 0.4375 |
| Vacancy rate | 18.13 |
| White | 60819 |
| Black | 2689 |
| Asian | 400 |
| Native | 592 |
| Hispanic/Latino | 9498 |
| Bachelor's or higher | 16604 |

## Districts

- [MI-04](/us/states/mi/districts/04.md) — 57% (congressional)
- [MI Senate District 20](/us/states/mi/districts/senate/20.md) — 54% (state senate)
- [MI Senate District 19](/us/states/mi/districts/senate/19.md) — 3% (state senate)
- [MI House District 39](/us/states/mi/districts/house/39.md) — 52% (state house)
- [MI House District 38](/us/states/mi/districts/house/38.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
