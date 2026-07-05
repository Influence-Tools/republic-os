---
type: Jurisdiction
title: "Fulton County, NY"
classification: county
fips: "36035"
state: "NY"
demographics:
  population: 52487
  population_under_18: 10491
  population_18_64: 31062
  population_65_plus: 10934
  median_household_income: 66533
  poverty_rate: 13.13
  homeownership_rate: 71.37
  unemployment_rate: 3.46
  median_home_value: 163100
  gini_index: 0.4392
  vacancy_rate: 18.91
  race_white: 46574
  race_black: 785
  race_asian: 479
  race_native: 2
  hispanic: 2294
  bachelors_plus: 10907
districts:
  - to: "us/states/ny/districts/21"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ny/districts/senate/49"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/house/118"
    rel: in-district
    area_weight: 0.8112
  - to: "us/states/ny/districts/house/112"
    rel: in-district
    area_weight: 0.1235
  - to: "us/states/ny/districts/house/114"
    rel: in-district
    area_weight: 0.0653
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Fulton County, NY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 52487 |
| Under 18 | 10491 |
| 18–64 | 31062 |
| 65+ | 10934 |
| Median household income | 66533 |
| Poverty rate | 13.13 |
| Homeownership rate | 71.37 |
| Unemployment rate | 3.46 |
| Median home value | 163100 |
| Gini index | 0.4392 |
| Vacancy rate | 18.91 |
| White | 46574 |
| Black | 785 |
| Asian | 479 |
| Native | 2 |
| Hispanic/Latino | 2294 |
| Bachelor's or higher | 10907 |

## Districts

- [NY-21](/us/states/ny/districts/21.md) — 100% (congressional)
- [NY Senate District 49](/us/states/ny/districts/senate/49.md) — 100% (state senate)
- [NY House District 118](/us/states/ny/districts/house/118.md) — 81% (state house)
- [NY House District 112](/us/states/ny/districts/house/112.md) — 12% (state house)
- [NY House District 114](/us/states/ny/districts/house/114.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
