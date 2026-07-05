---
type: Jurisdiction
title: "Johnson County, WY"
classification: county
fips: "56019"
state: "WY"
demographics:
  population: 8686
  population_under_18: 1676
  population_18_64: 4618
  population_65_plus: 2392
  median_household_income: 64871
  poverty_rate: 9.11
  homeownership_rate: 82.35
  unemployment_rate: 3.13
  median_home_value: 326800
  gini_index: 0.4426
  vacancy_rate: 15.6
  race_white: 7964
  race_black: 1
  race_asian: 47
  race_native: 144
  hispanic: 373
  bachelors_plus: 2769
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wy/districts/senate/22"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wy/districts/house/40"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Johnson County, WY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8686 |
| Under 18 | 1676 |
| 18–64 | 4618 |
| 65+ | 2392 |
| Median household income | 64871 |
| Poverty rate | 9.11 |
| Homeownership rate | 82.35 |
| Unemployment rate | 3.13 |
| Median home value | 326800 |
| Gini index | 0.4426 |
| Vacancy rate | 15.6 |
| White | 7964 |
| Black | 1 |
| Asian | 47 |
| Native | 144 |
| Hispanic/Latino | 373 |
| Bachelor's or higher | 2769 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 22](/us/states/wy/districts/senate/22.md) — 100% (state senate)
- [WY House District 40](/us/states/wy/districts/house/40.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
