---
type: Jurisdiction
title: "Virginia Beach city, VA"
classification: county
fips: "51810"
state: "VA"
demographics:
  population: 456349
  population_under_18: 99859
  population_18_64: 283975
  population_65_plus: 72515
  median_household_income: 92968
  poverty_rate: 8.59
  homeownership_rate: 65.15
  unemployment_rate: 3.96
  median_home_value: 382500
  gini_index: 0.4361
  vacancy_rate: 5.98
  race_white: 277439
  race_black: 85740
  race_asian: 33022
  race_native: 1042
  hispanic: 41512
  bachelors_plus: 179504
districts:
  - to: "us/states/va/districts/02"
    rel: in-district
    area_weight: 0.6153
  - to: "us/states/va/districts/senate/19"
    rel: in-district
    area_weight: 0.4076
  - to: "us/states/va/districts/senate/20"
    rel: in-district
    area_weight: 0.1243
  - to: "us/states/va/districts/senate/22"
    rel: in-district
    area_weight: 0.0844
  - to: "us/states/va/districts/house/98"
    rel: in-district
    area_weight: 0.3985
  - to: "us/states/va/districts/house/99"
    rel: in-district
    area_weight: 0.0809
  - to: "us/states/va/districts/house/97"
    rel: in-district
    area_weight: 0.0395
  - to: "us/states/va/districts/house/100"
    rel: in-district
    area_weight: 0.0347
  - to: "us/states/va/districts/house/95"
    rel: in-district
    area_weight: 0.0314
  - to: "us/states/va/districts/house/96"
    rel: in-district
    area_weight: 0.031
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Virginia Beach city, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 456349 |
| Under 18 | 99859 |
| 18–64 | 283975 |
| 65+ | 72515 |
| Median household income | 92968 |
| Poverty rate | 8.59 |
| Homeownership rate | 65.15 |
| Unemployment rate | 3.96 |
| Median home value | 382500 |
| Gini index | 0.4361 |
| Vacancy rate | 5.98 |
| White | 277439 |
| Black | 85740 |
| Asian | 33022 |
| Native | 1042 |
| Hispanic/Latino | 41512 |
| Bachelor's or higher | 179504 |

## Districts

- [VA-02](/us/states/va/districts/02.md) — 62% (congressional)
- [VA Senate District 19](/us/states/va/districts/senate/19.md) — 41% (state senate)
- [VA Senate District 20](/us/states/va/districts/senate/20.md) — 12% (state senate)
- [VA Senate District 22](/us/states/va/districts/senate/22.md) — 8% (state senate)
- [VA House District 98](/us/states/va/districts/house/98.md) — 40% (state house)
- [VA House District 99](/us/states/va/districts/house/99.md) — 8% (state house)
- [VA House District 97](/us/states/va/districts/house/97.md) — 4% (state house)
- [VA House District 100](/us/states/va/districts/house/100.md) — 3% (state house)
- [VA House District 95](/us/states/va/districts/house/95.md) — 3% (state house)
- [VA House District 96](/us/states/va/districts/house/96.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
