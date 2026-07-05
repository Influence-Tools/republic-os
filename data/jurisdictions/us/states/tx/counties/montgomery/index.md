---
type: Jurisdiction
title: "Montgomery County, TX"
classification: county
fips: "48339"
state: "TX"
demographics:
  population: 684432
  population_under_18: 177029
  population_18_64: 413346
  population_65_plus: 94057
  median_household_income: 97701
  poverty_rate: 9.44
  homeownership_rate: 71.77
  unemployment_rate: 4.55
  median_home_value: 346200
  gini_index: 0.4695
  vacancy_rate: 6.95
  race_white: 456971
  race_black: 43569
  race_asian: 23374
  race_native: 3486
  hispanic: 191006
  bachelors_plus: 236051
districts:
  - to: "us/states/tx/districts/08"
    rel: in-district
    area_weight: 0.6675
  - to: "us/states/tx/districts/02"
    rel: in-district
    area_weight: 0.3321
  - to: "us/states/tx/districts/senate/4"
    rel: in-district
    area_weight: 0.7618
  - to: "us/states/tx/districts/senate/18"
    rel: in-district
    area_weight: 0.1512
  - to: "us/states/tx/districts/senate/7"
    rel: in-district
    area_weight: 0.0868
  - to: "us/states/tx/districts/house/16"
    rel: in-district
    area_weight: 0.4969
  - to: "us/states/tx/districts/house/3"
    rel: in-district
    area_weight: 0.3254
  - to: "us/states/tx/districts/house/15"
    rel: in-district
    area_weight: 0.1003
  - to: "us/states/tx/districts/house/18"
    rel: in-district
    area_weight: 0.0772
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Montgomery County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 684432 |
| Under 18 | 177029 |
| 18–64 | 413346 |
| 65+ | 94057 |
| Median household income | 97701 |
| Poverty rate | 9.44 |
| Homeownership rate | 71.77 |
| Unemployment rate | 4.55 |
| Median home value | 346200 |
| Gini index | 0.4695 |
| Vacancy rate | 6.95 |
| White | 456971 |
| Black | 43569 |
| Asian | 23374 |
| Native | 3486 |
| Hispanic/Latino | 191006 |
| Bachelor's or higher | 236051 |

## Districts

- [TX-08](/us/states/tx/districts/08.md) — 67% (congressional)
- [TX-02](/us/states/tx/districts/02.md) — 33% (congressional)
- [TX Senate District 4](/us/states/tx/districts/senate/4.md) — 76% (state senate)
- [TX Senate District 18](/us/states/tx/districts/senate/18.md) — 15% (state senate)
- [TX Senate District 7](/us/states/tx/districts/senate/7.md) — 9% (state senate)
- [TX House District 16](/us/states/tx/districts/house/16.md) — 50% (state house)
- [TX House District 3](/us/states/tx/districts/house/3.md) — 33% (state house)
- [TX House District 15](/us/states/tx/districts/house/15.md) — 10% (state house)
- [TX House District 18](/us/states/tx/districts/house/18.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
