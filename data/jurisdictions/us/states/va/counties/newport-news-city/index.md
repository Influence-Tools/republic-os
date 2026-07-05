---
type: Jurisdiction
title: "Newport News city, VA"
classification: county
fips: "51700"
state: "VA"
demographics:
  population: 184216
  population_under_18: 48924
  population_18_64: 69467
  population_65_plus: 65825
  median_household_income: 69634
  poverty_rate: 14.48
  homeownership_rate: 48.16
  unemployment_rate: 5.77
  median_home_value: 260600
  gini_index: 0.4521
  vacancy_rate: 7.24
  race_white: 75455
  race_black: 75866
  race_asian: 6120
  race_native: 500
  hispanic: 19873
  bachelors_plus: 50622
districts:
  - to: "us/states/va/districts/03"
    rel: in-district
    area_weight: 0.5996
  - to: "us/states/va/districts/senate/24"
    rel: in-district
    area_weight: 0.4019
  - to: "us/states/va/districts/senate/23"
    rel: in-district
    area_weight: 0.1849
  - to: "us/states/va/districts/house/70"
    rel: in-district
    area_weight: 0.2386
  - to: "us/states/va/districts/house/85"
    rel: in-district
    area_weight: 0.2175
  - to: "us/states/va/districts/house/69"
    rel: in-district
    area_weight: 0.1304
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Newport News city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 184216 |
| Under 18 | 48924 |
| 18–64 | 69467 |
| 65+ | 65825 |
| Median household income | 69634 |
| Poverty rate | 14.48 |
| Homeownership rate | 48.16 |
| Unemployment rate | 5.77 |
| Median home value | 260600 |
| Gini index | 0.4521 |
| Vacancy rate | 7.24 |
| White | 75455 |
| Black | 75866 |
| Asian | 6120 |
| Native | 500 |
| Hispanic/Latino | 19873 |
| Bachelor's or higher | 50622 |

## Districts

- [VA-03](/us/states/va/districts/03.md) — 60% (congressional)
- [VA Senate District 24](/us/states/va/districts/senate/24.md) — 40% (state senate)
- [VA Senate District 23](/us/states/va/districts/senate/23.md) — 18% (state senate)
- [VA House District 70](/us/states/va/districts/house/70.md) — 24% (state house)
- [VA House District 85](/us/states/va/districts/house/85.md) — 22% (state house)
- [VA House District 69](/us/states/va/districts/house/69.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
