---
type: Jurisdiction
title: "Prince Edward County, VA"
classification: county
fips: "51147"
state: "VA"
demographics:
  population: 21996
  population_under_18: 3349
  population_18_64: 14882
  population_65_plus: 3765
  median_household_income: 56315
  poverty_rate: 20.89
  homeownership_rate: 58.03
  unemployment_rate: 1.54
  median_home_value: 216600
  gini_index: 0.4916
  vacancy_rate: 17.03
  race_white: 13675
  race_black: 6549
  race_asian: 242
  race_native: 86
  hispanic: 1078
  bachelors_plus: 5353
districts:
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/9"
    rel: in-district
    area_weight: 0.7596
  - to: "us/states/va/districts/senate/10"
    rel: in-district
    area_weight: 0.2404
  - to: "us/states/va/districts/house/50"
    rel: in-district
    area_weight: 0.8166
  - to: "us/states/va/districts/house/56"
    rel: in-district
    area_weight: 0.1834
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Prince Edward County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21996 |
| Under 18 | 3349 |
| 18–64 | 14882 |
| 65+ | 3765 |
| Median household income | 56315 |
| Poverty rate | 20.89 |
| Homeownership rate | 58.03 |
| Unemployment rate | 1.54 |
| Median home value | 216600 |
| Gini index | 0.4916 |
| Vacancy rate | 17.03 |
| White | 13675 |
| Black | 6549 |
| Asian | 242 |
| Native | 86 |
| Hispanic/Latino | 1078 |
| Bachelor's or higher | 5353 |

## Districts

- [VA-05](/us/states/va/districts/05.md) — 100% (congressional)
- [VA Senate District 9](/us/states/va/districts/senate/9.md) — 76% (state senate)
- [VA Senate District 10](/us/states/va/districts/senate/10.md) — 24% (state senate)
- [VA House District 50](/us/states/va/districts/house/50.md) — 82% (state house)
- [VA House District 56](/us/states/va/districts/house/56.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
