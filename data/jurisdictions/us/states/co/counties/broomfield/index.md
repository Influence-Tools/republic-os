---
type: Jurisdiction
title: "Broomfield County, CO"
classification: county
fips: "08014"
state: "CO"
demographics:
  population: 76304
  population_under_18: 15615
  population_18_64: 48788
  population_65_plus: 11901
  median_household_income: 123874
  poverty_rate: 6.17
  homeownership_rate: 62.74
  unemployment_rate: 3.79
  median_home_value: 664500
  gini_index: 0.4
  vacancy_rate: 4.34
  race_white: 58017
  race_black: 849
  race_asian: 5338
  race_native: 412
  hispanic: 10780
  bachelors_plus: 46374
districts:
  - to: "us/states/co/districts/07"
    rel: in-district
    area_weight: 0.9767
  - to: "us/states/co/districts/02"
    rel: in-district
    area_weight: 0.0172
  - to: "us/states/co/districts/08"
    rel: in-district
    area_weight: 0.006
  - to: "us/states/co/districts/senate/25"
    rel: in-district
    area_weight: 0.9922
  - to: "us/states/co/districts/senate/17"
    rel: in-district
    area_weight: 0.0073
  - to: "us/states/co/districts/house/33"
    rel: in-district
    area_weight: 0.992
  - to: "us/states/co/districts/house/12"
    rel: in-district
    area_weight: 0.0072
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Broomfield County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 76304 |
| Under 18 | 15615 |
| 18–64 | 48788 |
| 65+ | 11901 |
| Median household income | 123874 |
| Poverty rate | 6.17 |
| Homeownership rate | 62.74 |
| Unemployment rate | 3.79 |
| Median home value | 664500 |
| Gini index | 0.4 |
| Vacancy rate | 4.34 |
| White | 58017 |
| Black | 849 |
| Asian | 5338 |
| Native | 412 |
| Hispanic/Latino | 10780 |
| Bachelor's or higher | 46374 |

## Districts

- [CO-07](/us/states/co/districts/07.md) — 98% (congressional)
- [CO-02](/us/states/co/districts/02.md) — 2% (congressional)
- [CO-08](/us/states/co/districts/08.md) — 1% (congressional)
- [CO Senate District 25](/us/states/co/districts/senate/25.md) — 99% (state senate)
- [CO Senate District 17](/us/states/co/districts/senate/17.md) — 1% (state senate)
- [CO House District 33](/us/states/co/districts/house/33.md) — 99% (state house)
- [CO House District 12](/us/states/co/districts/house/12.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
