---
type: Jurisdiction
title: "Cape Girardeau County, MO"
classification: county
fips: "29031"
state: "MO"
demographics:
  population: 82735
  population_under_18: 17657
  population_18_64: 50312
  population_65_plus: 14766
  median_household_income: 68464
  poverty_rate: 13.95
  homeownership_rate: 66.76
  unemployment_rate: 2.32
  median_home_value: 220700
  gini_index: 0.4606
  vacancy_rate: 10.06
  race_white: 69959
  race_black: 6109
  race_asian: 1361
  race_native: 255
  hispanic: 2439
  bachelors_plus: 24311
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/senate/27"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/146"
    rel: in-district
    area_weight: 0.7216
  - to: "us/states/mo/districts/house/151"
    rel: in-district
    area_weight: 0.2312
  - to: "us/states/mo/districts/house/147"
    rel: in-district
    area_weight: 0.0468
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Cape Girardeau County, MO

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 82735 |
| Under 18 | 17657 |
| 18–64 | 50312 |
| 65+ | 14766 |
| Median household income | 68464 |
| Poverty rate | 13.95 |
| Homeownership rate | 66.76 |
| Unemployment rate | 2.32 |
| Median home value | 220700 |
| Gini index | 0.4606 |
| Vacancy rate | 10.06 |
| White | 69959 |
| Black | 6109 |
| Asian | 1361 |
| Native | 255 |
| Hispanic/Latino | 2439 |
| Bachelor's or higher | 24311 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 27](/us/states/mo/districts/senate/27.md) — 100% (state senate)
- [MO House District 146](/us/states/mo/districts/house/146.md) — 72% (state house)
- [MO House District 151](/us/states/mo/districts/house/151.md) — 23% (state house)
- [MO House District 147](/us/states/mo/districts/house/147.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
