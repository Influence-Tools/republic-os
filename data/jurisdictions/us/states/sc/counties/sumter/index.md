---
type: Jurisdiction
title: "Sumter County, SC"
classification: county
fips: "45085"
state: "SC"
demographics:
  population: 104725
  population_under_18: 24823
  population_18_64: 61296
  population_65_plus: 18606
  median_household_income: 56693
  poverty_rate: 16.56
  homeownership_rate: 68.13
  unemployment_rate: 6.87
  median_home_value: 165300
  gini_index: 0.4615
  vacancy_rate: 13.66
  race_white: 46981
  race_black: 48127
  race_asian: 1553
  race_native: 568
  hispanic: 4655
  bachelors_plus: 22623
districts:
  - to: "us/states/sc/districts/05"
    rel: in-district
    area_weight: 0.6852
  - to: "us/states/sc/districts/06"
    rel: in-district
    area_weight: 0.314
  - to: "us/states/sc/districts/senate/35"
    rel: in-district
    area_weight: 0.5495
  - to: "us/states/sc/districts/senate/36"
    rel: in-district
    area_weight: 0.2924
  - to: "us/states/sc/districts/senate/29"
    rel: in-district
    area_weight: 0.1579
  - to: "us/states/sc/districts/house/64"
    rel: in-district
    area_weight: 0.3371
  - to: "us/states/sc/districts/house/50"
    rel: in-district
    area_weight: 0.3173
  - to: "us/states/sc/districts/house/51"
    rel: in-district
    area_weight: 0.2091
  - to: "us/states/sc/districts/house/67"
    rel: in-district
    area_weight: 0.1363
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Sumter County, SC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 104725 |
| Under 18 | 24823 |
| 18–64 | 61296 |
| 65+ | 18606 |
| Median household income | 56693 |
| Poverty rate | 16.56 |
| Homeownership rate | 68.13 |
| Unemployment rate | 6.87 |
| Median home value | 165300 |
| Gini index | 0.4615 |
| Vacancy rate | 13.66 |
| White | 46981 |
| Black | 48127 |
| Asian | 1553 |
| Native | 568 |
| Hispanic/Latino | 4655 |
| Bachelor's or higher | 22623 |

## Districts

- [SC-05](/us/states/sc/districts/05.md) — 69% (congressional)
- [SC-06](/us/states/sc/districts/06.md) — 31% (congressional)
- [SC Senate District 35](/us/states/sc/districts/senate/35.md) — 55% (state senate)
- [SC Senate District 36](/us/states/sc/districts/senate/36.md) — 29% (state senate)
- [SC Senate District 29](/us/states/sc/districts/senate/29.md) — 16% (state senate)
- [SC House District 64](/us/states/sc/districts/house/64.md) — 34% (state house)
- [SC House District 50](/us/states/sc/districts/house/50.md) — 32% (state house)
- [SC House District 51](/us/states/sc/districts/house/51.md) — 21% (state house)
- [SC House District 67](/us/states/sc/districts/house/67.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
