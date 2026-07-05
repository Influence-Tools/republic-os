---
type: Jurisdiction
title: "Athens County, OH"
classification: county
fips: "39009"
state: "OH"
demographics:
  population: 61737
  population_under_18: 9152
  population_18_64: 43283
  population_65_plus: 9302
  median_household_income: 56001
  poverty_rate: 21.49
  homeownership_rate: 60.39
  unemployment_rate: 6.52
  median_home_value: 185000
  gini_index: 0.4933
  vacancy_rate: 13.06
  race_white: 55392
  race_black: 1368
  race_asian: 1299
  race_native: 24
  hispanic: 1422
  bachelors_plus: 19494
districts:
  - to: "us/states/oh/districts/12"
    rel: in-district
    area_weight: 0.9979
  - to: "us/states/oh/districts/senate/30"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/house/94"
    rel: in-district
    area_weight: 0.732
  - to: "us/states/oh/districts/house/95"
    rel: in-district
    area_weight: 0.2678
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Athens County, OH

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 61737 |
| Under 18 | 9152 |
| 18–64 | 43283 |
| 65+ | 9302 |
| Median household income | 56001 |
| Poverty rate | 21.49 |
| Homeownership rate | 60.39 |
| Unemployment rate | 6.52 |
| Median home value | 185000 |
| Gini index | 0.4933 |
| Vacancy rate | 13.06 |
| White | 55392 |
| Black | 1368 |
| Asian | 1299 |
| Native | 24 |
| Hispanic/Latino | 1422 |
| Bachelor's or higher | 19494 |

## Districts

- [OH-12](/us/states/oh/districts/12.md) — 100% (congressional)
- [OH Senate District 30](/us/states/oh/districts/senate/30.md) — 100% (state senate)
- [OH House District 94](/us/states/oh/districts/house/94.md) — 73% (state house)
- [OH House District 95](/us/states/oh/districts/house/95.md) — 27% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
