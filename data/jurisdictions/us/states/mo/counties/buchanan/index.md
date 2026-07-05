---
type: Jurisdiction
title: "Buchanan County, MO"
classification: county
fips: "29021"
state: "MO"
demographics:
  population: 83568
  population_under_18: 18644
  population_18_64: 50347
  population_65_plus: 14577
  median_household_income: 62158
  poverty_rate: 16.02
  homeownership_rate: 66.34
  unemployment_rate: 4.16
  median_home_value: 166300
  gini_index: 0.4726
  vacancy_rate: 13.08
  race_white: 67554
  race_black: 4855
  race_asian: 930
  race_native: 352
  hispanic: 6318
  bachelors_plus: 18043
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/senate/34"
    rel: in-district
    area_weight: 0.5495
  - to: "us/states/mo/districts/senate/12"
    rel: in-district
    area_weight: 0.4503
  - to: "us/states/mo/districts/house/13"
    rel: in-district
    area_weight: 0.7318
  - to: "us/states/mo/districts/house/11"
    rel: in-district
    area_weight: 0.2122
  - to: "us/states/mo/districts/house/10"
    rel: in-district
    area_weight: 0.0556
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Buchanan County, MO

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 83568 |
| Under 18 | 18644 |
| 18–64 | 50347 |
| 65+ | 14577 |
| Median household income | 62158 |
| Poverty rate | 16.02 |
| Homeownership rate | 66.34 |
| Unemployment rate | 4.16 |
| Median home value | 166300 |
| Gini index | 0.4726 |
| Vacancy rate | 13.08 |
| White | 67554 |
| Black | 4855 |
| Asian | 930 |
| Native | 352 |
| Hispanic/Latino | 6318 |
| Bachelor's or higher | 18043 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 34](/us/states/mo/districts/senate/34.md) — 55% (state senate)
- [MO Senate District 12](/us/states/mo/districts/senate/12.md) — 45% (state senate)
- [MO House District 13](/us/states/mo/districts/house/13.md) — 73% (state house)
- [MO House District 11](/us/states/mo/districts/house/11.md) — 21% (state house)
- [MO House District 10](/us/states/mo/districts/house/10.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
