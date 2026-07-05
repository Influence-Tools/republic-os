---
type: Jurisdiction
title: "Cole County, MO"
classification: county
fips: "29051"
state: "MO"
demographics:
  population: 77032
  population_under_18: 17011
  population_18_64: 46131
  population_65_plus: 13890
  median_household_income: 74876
  poverty_rate: 9.05
  homeownership_rate: 67.87
  unemployment_rate: 2.93
  median_home_value: 229600
  gini_index: 0.4239
  vacancy_rate: 7.3
  race_white: 61853
  race_black: 7563
  race_asian: 1130
  race_native: 248
  hispanic: 2807
  bachelors_plus: 28224
districts:
  - to: "us/states/mo/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/6"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/59"
    rel: in-district
    area_weight: 0.9279
  - to: "us/states/mo/districts/house/60"
    rel: in-district
    area_weight: 0.0718
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Cole County, MO

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 77032 |
| Under 18 | 17011 |
| 18–64 | 46131 |
| 65+ | 13890 |
| Median household income | 74876 |
| Poverty rate | 9.05 |
| Homeownership rate | 67.87 |
| Unemployment rate | 2.93 |
| Median home value | 229600 |
| Gini index | 0.4239 |
| Vacancy rate | 7.3 |
| White | 61853 |
| Black | 7563 |
| Asian | 1130 |
| Native | 248 |
| Hispanic/Latino | 2807 |
| Bachelor's or higher | 28224 |

## Districts

- [MO-03](/us/states/mo/districts/03.md) — 100% (congressional)
- [MO Senate District 6](/us/states/mo/districts/senate/6.md) — 100% (state senate)
- [MO House District 59](/us/states/mo/districts/house/59.md) — 93% (state house)
- [MO House District 60](/us/states/mo/districts/house/60.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
