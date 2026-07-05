---
type: Jurisdiction
title: "Camden County, MO"
classification: county
fips: "29029"
state: "MO"
demographics:
  population: 43667
  population_under_18: 7489
  population_18_64: 23218
  population_65_plus: 12960
  median_household_income: 66387
  poverty_rate: 12.6
  homeownership_rate: 82.49
  unemployment_rate: 4.32
  median_home_value: 305400
  gini_index: 0.4648
  vacancy_rate: 55.27
  race_white: 40534
  race_black: 386
  race_asian: 274
  race_native: 54
  hispanic: 1526
  bachelors_plus: 11933
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 0.9286
  - to: "us/states/mo/districts/03"
    rel: in-district
    area_weight: 0.0714
  - to: "us/states/mo/districts/senate/6"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/123"
    rel: in-district
    area_weight: 0.7576
  - to: "us/states/mo/districts/house/142"
    rel: in-district
    area_weight: 0.2422
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Camden County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43667 |
| Under 18 | 7489 |
| 18–64 | 23218 |
| 65+ | 12960 |
| Median household income | 66387 |
| Poverty rate | 12.6 |
| Homeownership rate | 82.49 |
| Unemployment rate | 4.32 |
| Median home value | 305400 |
| Gini index | 0.4648 |
| Vacancy rate | 55.27 |
| White | 40534 |
| Black | 386 |
| Asian | 274 |
| Native | 54 |
| Hispanic/Latino | 1526 |
| Bachelor's or higher | 11933 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 93% (congressional)
- [MO-03](/us/states/mo/districts/03.md) — 7% (congressional)
- [MO Senate District 6](/us/states/mo/districts/senate/6.md) — 100% (state senate)
- [MO House District 123](/us/states/mo/districts/house/123.md) — 76% (state house)
- [MO House District 142](/us/states/mo/districts/house/142.md) — 24% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
