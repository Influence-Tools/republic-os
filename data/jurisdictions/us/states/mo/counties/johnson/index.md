---
type: Jurisdiction
title: "Johnson County, MO"
classification: county
fips: "29101"
state: "MO"
demographics:
  population: 54732
  population_under_18: 12108
  population_18_64: 35428
  population_65_plus: 7196
  median_household_income: 67272
  poverty_rate: 11.81
  homeownership_rate: 63.5
  unemployment_rate: 4.73
  median_home_value: 235700
  gini_index: 0.4005
  vacancy_rate: 7.23
  race_white: 46706
  race_black: 2380
  race_asian: 830
  race_native: 145
  hispanic: 2821
  bachelors_plus: 13054
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/31"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mo/districts/house/54"
    rel: in-district
    area_weight: 0.5188
  - to: "us/states/mo/districts/house/57"
    rel: in-district
    area_weight: 0.4809
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Johnson County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 54732 |
| Under 18 | 12108 |
| 18–64 | 35428 |
| 65+ | 7196 |
| Median household income | 67272 |
| Poverty rate | 11.81 |
| Homeownership rate | 63.5 |
| Unemployment rate | 4.73 |
| Median home value | 235700 |
| Gini index | 0.4005 |
| Vacancy rate | 7.23 |
| White | 46706 |
| Black | 2380 |
| Asian | 830 |
| Native | 145 |
| Hispanic/Latino | 2821 |
| Bachelor's or higher | 13054 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 100% (congressional)
- [MO Senate District 31](/us/states/mo/districts/senate/31.md) — 100% (state senate)
- [MO House District 54](/us/states/mo/districts/house/54.md) — 52% (state house)
- [MO House District 57](/us/states/mo/districts/house/57.md) — 48% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
