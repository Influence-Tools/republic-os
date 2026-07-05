---
type: Jurisdiction
title: "Butler County, OH"
classification: county
fips: "39017"
state: "OH"
demographics:
  population: 392876
  population_under_18: 91772
  population_18_64: 238766
  population_65_plus: 62338
  median_household_income: 81590
  poverty_rate: 11.82
  homeownership_rate: 69.93
  unemployment_rate: 5.07
  median_home_value: 258500
  gini_index: 0.4403
  vacancy_rate: 5.5
  race_white: 297734
  race_black: 32857
  race_asian: 17020
  race_native: 678
  hispanic: 27328
  bachelors_plus: 113091
districts:
  - to: "us/states/oh/districts/08"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/oh/districts/senate/4"
    rel: in-district
    area_weight: 0.8331
  - to: "us/states/oh/districts/senate/5"
    rel: in-district
    area_weight: 0.1667
  - to: "us/states/oh/districts/house/47"
    rel: in-district
    area_weight: 0.305
  - to: "us/states/oh/districts/house/45"
    rel: in-district
    area_weight: 0.2666
  - to: "us/states/oh/districts/house/46"
    rel: in-district
    area_weight: 0.2616
  - to: "us/states/oh/districts/house/40"
    rel: in-district
    area_weight: 0.1667
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Butler County, OH

County jurisdiction — 4 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 392876 |
| Under 18 | 91772 |
| 18–64 | 238766 |
| 65+ | 62338 |
| Median household income | 81590 |
| Poverty rate | 11.82 |
| Homeownership rate | 69.93 |
| Unemployment rate | 5.07 |
| Median home value | 258500 |
| Gini index | 0.4403 |
| Vacancy rate | 5.5 |
| White | 297734 |
| Black | 32857 |
| Asian | 17020 |
| Native | 678 |
| Hispanic/Latino | 27328 |
| Bachelor's or higher | 113091 |

## Districts

- [OH-08](/us/states/oh/districts/08.md) — 100% (congressional)
- [OH Senate District 4](/us/states/oh/districts/senate/4.md) — 83% (state senate)
- [OH Senate District 5](/us/states/oh/districts/senate/5.md) — 17% (state senate)
- [OH House District 47](/us/states/oh/districts/house/47.md) — 30% (state house)
- [OH House District 45](/us/states/oh/districts/house/45.md) — 27% (state house)
- [OH House District 46](/us/states/oh/districts/house/46.md) — 26% (state house)
- [OH House District 40](/us/states/oh/districts/house/40.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
