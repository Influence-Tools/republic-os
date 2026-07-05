---
type: Jurisdiction
title: "Camden County, NJ"
classification: county
fips: "34007"
state: "NJ"
demographics:
  population: 527257
  population_under_18: 119695
  population_18_64: 320368
  population_65_plus: 87194
  median_household_income: 88755
  poverty_rate: 12.4
  homeownership_rate: 64.69
  unemployment_rate: 6.89
  median_home_value: 287100
  gini_index: 0.4661
  vacancy_rate: 5.26
  race_white: 287612
  race_black: 101050
  race_asian: 31500
  race_native: 2484
  hispanic: 101417
  bachelors_plus: 185588
districts:
  - to: "us/states/nj/districts/01"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/nj/districts/senate/4"
    rel: in-district
    area_weight: 0.5244
  - to: "us/states/nj/districts/senate/6"
    rel: in-district
    area_weight: 0.302
  - to: "us/states/nj/districts/senate/5"
    rel: in-district
    area_weight: 0.1724
  - to: "us/states/nj/districts/house/4"
    rel: in-district
    area_weight: 0.5244
  - to: "us/states/nj/districts/house/6"
    rel: in-district
    area_weight: 0.302
  - to: "us/states/nj/districts/house/5"
    rel: in-district
    area_weight: 0.1724
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nj]
timestamp: "2026-07-03"
---

# Camden County, NJ

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 527257 |
| Under 18 | 119695 |
| 18–64 | 320368 |
| 65+ | 87194 |
| Median household income | 88755 |
| Poverty rate | 12.4 |
| Homeownership rate | 64.69 |
| Unemployment rate | 6.89 |
| Median home value | 287100 |
| Gini index | 0.4661 |
| Vacancy rate | 5.26 |
| White | 287612 |
| Black | 101050 |
| Asian | 31500 |
| Native | 2484 |
| Hispanic/Latino | 101417 |
| Bachelor's or higher | 185588 |

## Districts

- [NJ-01](/us/states/nj/districts/01.md) — 100% (congressional)
- [NJ Senate District 4](/us/states/nj/districts/senate/4.md) — 52% (state senate)
- [NJ Senate District 6](/us/states/nj/districts/senate/6.md) — 30% (state senate)
- [NJ Senate District 5](/us/states/nj/districts/senate/5.md) — 17% (state senate)
- [NJ House District 4](/us/states/nj/districts/house/4.md) — 52% (state house)
- [NJ House District 6](/us/states/nj/districts/house/6.md) — 30% (state house)
- [NJ House District 5](/us/states/nj/districts/house/5.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
