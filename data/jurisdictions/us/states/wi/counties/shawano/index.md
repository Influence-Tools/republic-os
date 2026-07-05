---
type: Jurisdiction
title: "Shawano County, WI"
classification: county
fips: "55115"
state: "WI"
demographics:
  population: 41039
  population_under_18: 8687
  population_18_64: 23200
  population_65_plus: 9152
  median_household_income: 66479
  poverty_rate: 11.12
  homeownership_rate: 77.53
  unemployment_rate: 2.59
  median_home_value: 194000
  gini_index: 0.4298
  vacancy_rate: 16.57
  race_white: 34965
  race_black: 245
  race_asian: 262
  race_native: 2485
  hispanic: 1334
  bachelors_plus: 7447
districts:
  - to: "us/states/wi/districts/08"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wi/districts/senate/2"
    rel: in-district
    area_weight: 0.6443
  - to: "us/states/wi/districts/senate/29"
    rel: in-district
    area_weight: 0.2777
  - to: "us/states/wi/districts/senate/12"
    rel: in-district
    area_weight: 0.078
  - to: "us/states/wi/districts/house/6"
    rel: in-district
    area_weight: 0.6443
  - to: "us/states/wi/districts/house/87"
    rel: in-district
    area_weight: 0.2777
  - to: "us/states/wi/districts/house/35"
    rel: in-district
    area_weight: 0.078
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Shawano County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 41039 |
| Under 18 | 8687 |
| 18–64 | 23200 |
| 65+ | 9152 |
| Median household income | 66479 |
| Poverty rate | 11.12 |
| Homeownership rate | 77.53 |
| Unemployment rate | 2.59 |
| Median home value | 194000 |
| Gini index | 0.4298 |
| Vacancy rate | 16.57 |
| White | 34965 |
| Black | 245 |
| Asian | 262 |
| Native | 2485 |
| Hispanic/Latino | 1334 |
| Bachelor's or higher | 7447 |

## Districts

- [WI-08](/us/states/wi/districts/08.md) — 100% (congressional)
- [WI Senate District 2](/us/states/wi/districts/senate/2.md) — 64% (state senate)
- [WI Senate District 29](/us/states/wi/districts/senate/29.md) — 28% (state senate)
- [WI Senate District 12](/us/states/wi/districts/senate/12.md) — 8% (state senate)
- [WI House District 6](/us/states/wi/districts/house/6.md) — 64% (state house)
- [WI House District 87](/us/states/wi/districts/house/87.md) — 28% (state house)
- [WI House District 35](/us/states/wi/districts/house/35.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
