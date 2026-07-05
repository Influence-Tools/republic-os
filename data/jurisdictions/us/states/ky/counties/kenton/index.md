---
type: Jurisdiction
title: "Kenton County, KY"
classification: county
fips: "21117"
state: "KY"
demographics:
  population: 171288
  population_under_18: 39980
  population_18_64: 104350
  population_65_plus: 26958
  median_household_income: 80548
  poverty_rate: 11.85
  homeownership_rate: 70.74
  unemployment_rate: 4.33
  median_home_value: 244400
  gini_index: 0.4576
  vacancy_rate: 7.99
  race_white: 147467
  race_black: 6717
  race_asian: 2001
  race_native: 283
  hispanic: 8330
  bachelors_plus: 59445
districts:
  - to: "us/states/ky/districts/04"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ky/districts/senate/17"
    rel: in-district
    area_weight: 0.4611
  - to: "us/states/ky/districts/senate/23"
    rel: in-district
    area_weight: 0.3702
  - to: "us/states/ky/districts/senate/20"
    rel: in-district
    area_weight: 0.165
  - to: "us/states/ky/districts/house/78"
    rel: in-district
    area_weight: 0.4286
  - to: "us/states/ky/districts/house/64"
    rel: in-district
    area_weight: 0.2133
  - to: "us/states/ky/districts/house/65"
    rel: in-district
    area_weight: 0.11
  - to: "us/states/ky/districts/house/61"
    rel: in-district
    area_weight: 0.0927
  - to: "us/states/ky/districts/house/63"
    rel: in-district
    area_weight: 0.0927
  - to: "us/states/ky/districts/house/69"
    rel: in-district
    area_weight: 0.0621
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Kenton County, KY

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 171288 |
| Under 18 | 39980 |
| 18–64 | 104350 |
| 65+ | 26958 |
| Median household income | 80548 |
| Poverty rate | 11.85 |
| Homeownership rate | 70.74 |
| Unemployment rate | 4.33 |
| Median home value | 244400 |
| Gini index | 0.4576 |
| Vacancy rate | 7.99 |
| White | 147467 |
| Black | 6717 |
| Asian | 2001 |
| Native | 283 |
| Hispanic/Latino | 8330 |
| Bachelor's or higher | 59445 |

## Districts

- [KY-04](/us/states/ky/districts/04.md) — 100% (congressional)
- [KY Senate District 17](/us/states/ky/districts/senate/17.md) — 46% (state senate)
- [KY Senate District 23](/us/states/ky/districts/senate/23.md) — 37% (state senate)
- [KY Senate District 20](/us/states/ky/districts/senate/20.md) — 16% (state senate)
- [KY House District 78](/us/states/ky/districts/house/78.md) — 43% (state house)
- [KY House District 64](/us/states/ky/districts/house/64.md) — 21% (state house)
- [KY House District 65](/us/states/ky/districts/house/65.md) — 11% (state house)
- [KY House District 61](/us/states/ky/districts/house/61.md) — 9% (state house)
- [KY House District 63](/us/states/ky/districts/house/63.md) — 9% (state house)
- [KY House District 69](/us/states/ky/districts/house/69.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
