---
type: Jurisdiction
title: "Deschutes County, OR"
classification: county
fips: "41017"
state: "OR"
demographics:
  population: 206334
  population_under_18: 39069
  population_18_64: 123395
  population_65_plus: 43870
  median_household_income: 92758
  poverty_rate: 8.8
  homeownership_rate: 69.98
  unemployment_rate: 4.4
  median_home_value: 650900
  gini_index: 0.4611
  vacancy_rate: 14.47
  race_white: 180121
  race_black: 882
  race_asian: 2235
  race_native: 1528
  hispanic: 19035
  bachelors_plus: 94825
districts:
  - to: "us/states/or/districts/02"
    rel: in-district
    area_weight: 0.6082
  - to: "us/states/or/districts/05"
    rel: in-district
    area_weight: 0.3914
  - to: "us/states/or/districts/senate/28"
    rel: in-district
    area_weight: 0.512
  - to: "us/states/or/districts/senate/30"
    rel: in-district
    area_weight: 0.3016
  - to: "us/states/or/districts/senate/27"
    rel: in-district
    area_weight: 0.1863
  - to: "us/states/or/districts/house/55"
    rel: in-district
    area_weight: 0.512
  - to: "us/states/or/districts/house/60"
    rel: in-district
    area_weight: 0.2223
  - to: "us/states/or/districts/house/53"
    rel: in-district
    area_weight: 0.1772
  - to: "us/states/or/districts/house/59"
    rel: in-district
    area_weight: 0.0793
  - to: "us/states/or/districts/house/54"
    rel: in-district
    area_weight: 0.0092
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Deschutes County, OR

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 206334 |
| Under 18 | 39069 |
| 18–64 | 123395 |
| 65+ | 43870 |
| Median household income | 92758 |
| Poverty rate | 8.8 |
| Homeownership rate | 69.98 |
| Unemployment rate | 4.4 |
| Median home value | 650900 |
| Gini index | 0.4611 |
| Vacancy rate | 14.47 |
| White | 180121 |
| Black | 882 |
| Asian | 2235 |
| Native | 1528 |
| Hispanic/Latino | 19035 |
| Bachelor's or higher | 94825 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 61% (congressional)
- [OR-05](/us/states/or/districts/05.md) — 39% (congressional)
- [OR Senate District 28](/us/states/or/districts/senate/28.md) — 51% (state senate)
- [OR Senate District 30](/us/states/or/districts/senate/30.md) — 30% (state senate)
- [OR Senate District 27](/us/states/or/districts/senate/27.md) — 19% (state senate)
- [OR House District 55](/us/states/or/districts/house/55.md) — 51% (state house)
- [OR House District 60](/us/states/or/districts/house/60.md) — 22% (state house)
- [OR House District 53](/us/states/or/districts/house/53.md) — 18% (state house)
- [OR House District 59](/us/states/or/districts/house/59.md) — 8% (state house)
- [OR House District 54](/us/states/or/districts/house/54.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
