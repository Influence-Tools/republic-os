---
type: Jurisdiction
title: "Stark County, OH"
classification: county
fips: "39151"
state: "OH"
demographics:
  population: 373713
  population_under_18: 80525
  population_18_64: 216561
  population_65_plus: 76627
  median_household_income: 67934
  poverty_rate: 12.46
  homeownership_rate: 69.23
  unemployment_rate: 3.88
  median_home_value: 186400
  gini_index: 0.4366
  vacancy_rate: 7.14
  race_white: 315829
  race_black: 26619
  race_asian: 3361
  race_native: 404
  hispanic: 11359
  bachelors_plus: 92255
districts:
  - to: "us/states/oh/districts/06"
    rel: in-district
    area_weight: 0.6451
  - to: "us/states/oh/districts/13"
    rel: in-district
    area_weight: 0.3544
  - to: "us/states/oh/districts/senate/29"
    rel: in-district
    area_weight: 0.7853
  - to: "us/states/oh/districts/senate/31"
    rel: in-district
    area_weight: 0.2145
  - to: "us/states/oh/districts/house/50"
    rel: in-district
    area_weight: 0.3914
  - to: "us/states/oh/districts/house/48"
    rel: in-district
    area_weight: 0.2847
  - to: "us/states/oh/districts/house/51"
    rel: in-district
    area_weight: 0.2141
  - to: "us/states/oh/districts/house/49"
    rel: in-district
    area_weight: 0.1092
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Stark County, OH

County jurisdiction — 6 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 373713 |
| Under 18 | 80525 |
| 18–64 | 216561 |
| 65+ | 76627 |
| Median household income | 67934 |
| Poverty rate | 12.46 |
| Homeownership rate | 69.23 |
| Unemployment rate | 3.88 |
| Median home value | 186400 |
| Gini index | 0.4366 |
| Vacancy rate | 7.14 |
| White | 315829 |
| Black | 26619 |
| Asian | 3361 |
| Native | 404 |
| Hispanic/Latino | 11359 |
| Bachelor's or higher | 92255 |

## Districts

- [OH-06](/us/states/oh/districts/06.md) — 65% (congressional)
- [OH-13](/us/states/oh/districts/13.md) — 35% (congressional)
- [OH Senate District 29](/us/states/oh/districts/senate/29.md) — 79% (state senate)
- [OH Senate District 31](/us/states/oh/districts/senate/31.md) — 21% (state senate)
- [OH House District 50](/us/states/oh/districts/house/50.md) — 39% (state house)
- [OH House District 48](/us/states/oh/districts/house/48.md) — 28% (state house)
- [OH House District 51](/us/states/oh/districts/house/51.md) — 21% (state house)
- [OH House District 49](/us/states/oh/districts/house/49.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
