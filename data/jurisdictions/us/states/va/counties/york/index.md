---
type: Jurisdiction
title: "York County, VA"
classification: county
fips: "51199"
state: "VA"
demographics:
  population: 71410
  population_under_18: 18212
  population_18_64: 20508
  population_65_plus: 32690
  median_household_income: 108815
  poverty_rate: 5.23
  homeownership_rate: 71.06
  unemployment_rate: 3.89
  median_home_value: 477300
  gini_index: 0.4082
  vacancy_rate: 3.63
  race_white: 48216
  race_black: 8962
  race_asian: 4238
  race_native: 0
  hispanic: 5896
  bachelors_plus: 34118
districts:
  - to: "us/states/va/districts/01"
    rel: in-district
    area_weight: 0.5835
  - to: "us/states/va/districts/senate/24"
    rel: in-district
    area_weight: 0.5799
  - to: "us/states/va/districts/house/69"
    rel: in-district
    area_weight: 0.541
  - to: "us/states/va/districts/house/86"
    rel: in-district
    area_weight: 0.0388
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# York County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 71410 |
| Under 18 | 18212 |
| 18–64 | 20508 |
| 65+ | 32690 |
| Median household income | 108815 |
| Poverty rate | 5.23 |
| Homeownership rate | 71.06 |
| Unemployment rate | 3.89 |
| Median home value | 477300 |
| Gini index | 0.4082 |
| Vacancy rate | 3.63 |
| White | 48216 |
| Black | 8962 |
| Asian | 4238 |
| Native | 0 |
| Hispanic/Latino | 5896 |
| Bachelor's or higher | 34118 |

## Districts

- [VA-01](/us/states/va/districts/01.md) — 58% (congressional)
- [VA Senate District 24](/us/states/va/districts/senate/24.md) — 58% (state senate)
- [VA House District 69](/us/states/va/districts/house/69.md) — 54% (state house)
- [VA House District 86](/us/states/va/districts/house/86.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
