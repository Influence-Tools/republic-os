---
type: Jurisdiction
title: "Louisa County, VA"
classification: county
fips: "51109"
state: "VA"
demographics:
  population: 39980
  population_under_18: 7993
  population_18_64: 23583
  population_65_plus: 8404
  median_household_income: 86689
  poverty_rate: 10.03
  homeownership_rate: 82.23
  unemployment_rate: 5.84
  median_home_value: 315300
  gini_index: 0.4414
  vacancy_rate: 15.27
  race_white: 30890
  race_black: 4640
  race_asian: 242
  race_native: 183
  hispanic: 1659
  bachelors_plus: 12339
districts:
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 0.9966
  - to: "us/states/va/districts/senate/10"
    rel: in-district
    area_weight: 0.7778
  - to: "us/states/va/districts/senate/11"
    rel: in-district
    area_weight: 0.2219
  - to: "us/states/va/districts/house/59"
    rel: in-district
    area_weight: 0.7777
  - to: "us/states/va/districts/house/55"
    rel: in-district
    area_weight: 0.2219
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Louisa County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39980 |
| Under 18 | 7993 |
| 18–64 | 23583 |
| 65+ | 8404 |
| Median household income | 86689 |
| Poverty rate | 10.03 |
| Homeownership rate | 82.23 |
| Unemployment rate | 5.84 |
| Median home value | 315300 |
| Gini index | 0.4414 |
| Vacancy rate | 15.27 |
| White | 30890 |
| Black | 4640 |
| Asian | 242 |
| Native | 183 |
| Hispanic/Latino | 1659 |
| Bachelor's or higher | 12339 |

## Districts

- [VA-05](/us/states/va/districts/05.md) — 100% (congressional)
- [VA Senate District 10](/us/states/va/districts/senate/10.md) — 78% (state senate)
- [VA Senate District 11](/us/states/va/districts/senate/11.md) — 22% (state senate)
- [VA House District 59](/us/states/va/districts/house/59.md) — 78% (state house)
- [VA House District 55](/us/states/va/districts/house/55.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
