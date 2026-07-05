---
type: Jurisdiction
title: "St. Francis County, AR"
classification: county
fips: "05123"
state: "AR"
demographics:
  population: 22400
  population_under_18: 4753
  population_18_64: 13639
  population_65_plus: 4008
  median_household_income: 42574
  poverty_rate: 28.47
  homeownership_rate: 55.49
  unemployment_rate: 9.23
  median_home_value: 90900
  gini_index: 0.4894
  vacancy_rate: 18.67
  race_white: 9185
  race_black: 12215
  race_asian: 30
  race_native: 68
  hispanic: 821
  bachelors_plus: 3217
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/10"
    rel: in-district
    area_weight: 0.556
  - to: "us/states/ar/districts/senate/9"
    rel: in-district
    area_weight: 0.444
  - to: "us/states/ar/districts/house/63"
    rel: in-district
    area_weight: 0.4746
  - to: "us/states/ar/districts/house/37"
    rel: in-district
    area_weight: 0.4625
  - to: "us/states/ar/districts/house/62"
    rel: in-district
    area_weight: 0.0628
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# St. Francis County, AR

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22400 |
| Under 18 | 4753 |
| 18–64 | 13639 |
| 65+ | 4008 |
| Median household income | 42574 |
| Poverty rate | 28.47 |
| Homeownership rate | 55.49 |
| Unemployment rate | 9.23 |
| Median home value | 90900 |
| Gini index | 0.4894 |
| Vacancy rate | 18.67 |
| White | 9185 |
| Black | 12215 |
| Asian | 30 |
| Native | 68 |
| Hispanic/Latino | 821 |
| Bachelor's or higher | 3217 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 10](/us/states/ar/districts/senate/10.md) — 56% (state senate)
- [AR Senate District 9](/us/states/ar/districts/senate/9.md) — 44% (state senate)
- [AR House District 63](/us/states/ar/districts/house/63.md) — 47% (state house)
- [AR House District 37](/us/states/ar/districts/house/37.md) — 46% (state house)
- [AR House District 62](/us/states/ar/districts/house/62.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
