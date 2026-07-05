---
type: Jurisdiction
title: "Franklin County, ME"
classification: county
fips: "23007"
state: "ME"
demographics:
  population: 30413
  population_under_18: 5201
  population_18_64: 18001
  population_65_plus: 7211
  median_household_income: 58675
  poverty_rate: 12.16
  homeownership_rate: 76.26
  unemployment_rate: 4.6
  median_home_value: 194700
  gini_index: 0.4559
  vacancy_rate: 40.31
  race_white: 28401
  race_black: 261
  race_asian: 208
  race_native: 50
  hispanic: 513
  bachelors_plus: 9706
districts:
  - to: "us/states/me/districts/02"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/me/districts/senate/19"
    rel: in-district
    area_weight: 0.6609
  - to: "us/states/me/districts/senate/5"
    rel: in-district
    area_weight: 0.3389
  - to: "us/states/me/districts/house/73"
    rel: in-district
    area_weight: 0.7062
  - to: "us/states/me/districts/house/74"
    rel: in-district
    area_weight: 0.1857
  - to: "us/states/me/districts/house/75"
    rel: in-district
    area_weight: 0.0532
  - to: "us/states/me/districts/house/76"
    rel: in-district
    area_weight: 0.028
  - to: "us/states/me/districts/house/58"
    rel: in-district
    area_weight: 0.0267
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, me]
timestamp: "2026-07-03"
---

# Franklin County, ME

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30413 |
| Under 18 | 5201 |
| 18–64 | 18001 |
| 65+ | 7211 |
| Median household income | 58675 |
| Poverty rate | 12.16 |
| Homeownership rate | 76.26 |
| Unemployment rate | 4.6 |
| Median home value | 194700 |
| Gini index | 0.4559 |
| Vacancy rate | 40.31 |
| White | 28401 |
| Black | 261 |
| Asian | 208 |
| Native | 50 |
| Hispanic/Latino | 513 |
| Bachelor's or higher | 9706 |

## Districts

- [ME-02](/us/states/me/districts/02.md) — 100% (congressional)
- [ME Senate District 19](/us/states/me/districts/senate/19.md) — 66% (state senate)
- [ME Senate District 5](/us/states/me/districts/senate/5.md) — 34% (state senate)
- [ME House District 73](/us/states/me/districts/house/73.md) — 71% (state house)
- [ME House District 74](/us/states/me/districts/house/74.md) — 19% (state house)
- [ME House District 75](/us/states/me/districts/house/75.md) — 5% (state house)
- [ME House District 76](/us/states/me/districts/house/76.md) — 3% (state house)
- [ME House District 58](/us/states/me/districts/house/58.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
