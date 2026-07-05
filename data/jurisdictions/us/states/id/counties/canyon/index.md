---
type: Jurisdiction
title: "Canyon County, ID"
classification: county
fips: "16027"
state: "ID"
demographics:
  population: 250790
  population_under_18: 67038
  population_18_64: 147285
  population_65_plus: 36467
  median_household_income: 76488
  poverty_rate: 10.51
  homeownership_rate: 75.54
  unemployment_rate: 3.66
  median_home_value: 390000
  gini_index: 0.3947
  vacancy_rate: 3.44
  race_white: 182916
  race_black: 1871
  race_asian: 2154
  race_native: 2451
  hispanic: 65197
  bachelors_plus: 48359
districts:
  - to: "us/states/id/districts/01"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/id/districts/senate/9"
    rel: in-district
    area_weight: 0.3254
  - to: "us/states/id/districts/senate/23"
    rel: in-district
    area_weight: 0.3164
  - to: "us/states/id/districts/senate/10"
    rel: in-district
    area_weight: 0.2364
  - to: "us/states/id/districts/senate/13"
    rel: in-district
    area_weight: 0.0519
  - to: "us/states/id/districts/senate/11"
    rel: in-district
    area_weight: 0.0367
  - to: "us/states/id/districts/senate/12"
    rel: in-district
    area_weight: 0.0331
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Canyon County, ID

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 250790 |
| Under 18 | 67038 |
| 18–64 | 147285 |
| 65+ | 36467 |
| Median household income | 76488 |
| Poverty rate | 10.51 |
| Homeownership rate | 75.54 |
| Unemployment rate | 3.66 |
| Median home value | 390000 |
| Gini index | 0.3947 |
| Vacancy rate | 3.44 |
| White | 182916 |
| Black | 1871 |
| Asian | 2154 |
| Native | 2451 |
| Hispanic/Latino | 65197 |
| Bachelor's or higher | 48359 |

## Districts

- [ID-01](/us/states/id/districts/01.md) — 100% (congressional)
- [ID Senate District 9](/us/states/id/districts/senate/9.md) — 33% (state senate)
- [ID Senate District 23](/us/states/id/districts/senate/23.md) — 32% (state senate)
- [ID Senate District 10](/us/states/id/districts/senate/10.md) — 24% (state senate)
- [ID Senate District 13](/us/states/id/districts/senate/13.md) — 5% (state senate)
- [ID Senate District 11](/us/states/id/districts/senate/11.md) — 4% (state senate)
- [ID Senate District 12](/us/states/id/districts/senate/12.md) — 3% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
