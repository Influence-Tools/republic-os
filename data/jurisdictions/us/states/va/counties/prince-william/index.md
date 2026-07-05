---
type: Jurisdiction
title: "Prince William County, VA"
classification: county
fips: "51153"
state: "VA"
demographics:
  population: 488880
  population_under_18: 129142
  population_18_64: 304460
  population_65_plus: 55278
  median_household_income: 131402
  poverty_rate: 6.19
  homeownership_rate: 74.26
  unemployment_rate: 4.8
  median_home_value: 530100
  gini_index: 0.3857
  vacancy_rate: 3.12
  race_white: 211371
  race_black: 97931
  race_asian: 48981
  race_native: 3271
  hispanic: 127463
  bachelors_plus: 199158
districts:
  - to: "us/states/va/districts/10"
    rel: in-district
    area_weight: 0.6034
  - to: "us/states/va/districts/07"
    rel: in-district
    area_weight: 0.3945
  - to: "us/states/va/districts/senate/29"
    rel: in-district
    area_weight: 0.5535
  - to: "us/states/va/districts/senate/30"
    rel: in-district
    area_weight: 0.3159
  - to: "us/states/va/districts/senate/33"
    rel: in-district
    area_weight: 0.1165
  - to: "us/states/va/districts/house/22"
    rel: in-district
    area_weight: 0.2982
  - to: "us/states/va/districts/house/21"
    rel: in-district
    area_weight: 0.2476
  - to: "us/states/va/districts/house/23"
    rel: in-district
    area_weight: 0.2192
  - to: "us/states/va/districts/house/25"
    rel: in-district
    area_weight: 0.0951
  - to: "us/states/va/districts/house/24"
    rel: in-district
    area_weight: 0.0702
  - to: "us/states/va/districts/house/19"
    rel: in-district
    area_weight: 0.037
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Prince William County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 488880 |
| Under 18 | 129142 |
| 18–64 | 304460 |
| 65+ | 55278 |
| Median household income | 131402 |
| Poverty rate | 6.19 |
| Homeownership rate | 74.26 |
| Unemployment rate | 4.8 |
| Median home value | 530100 |
| Gini index | 0.3857 |
| Vacancy rate | 3.12 |
| White | 211371 |
| Black | 97931 |
| Asian | 48981 |
| Native | 3271 |
| Hispanic/Latino | 127463 |
| Bachelor's or higher | 199158 |

## Districts

- [VA-10](/us/states/va/districts/10.md) — 60% (congressional)
- [VA-07](/us/states/va/districts/07.md) — 39% (congressional)
- [VA Senate District 29](/us/states/va/districts/senate/29.md) — 55% (state senate)
- [VA Senate District 30](/us/states/va/districts/senate/30.md) — 32% (state senate)
- [VA Senate District 33](/us/states/va/districts/senate/33.md) — 12% (state senate)
- [VA House District 22](/us/states/va/districts/house/22.md) — 30% (state house)
- [VA House District 21](/us/states/va/districts/house/21.md) — 25% (state house)
- [VA House District 23](/us/states/va/districts/house/23.md) — 22% (state house)
- [VA House District 25](/us/states/va/districts/house/25.md) — 10% (state house)
- [VA House District 24](/us/states/va/districts/house/24.md) — 7% (state house)
- [VA House District 19](/us/states/va/districts/house/19.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
