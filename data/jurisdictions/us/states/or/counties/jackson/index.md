---
type: Jurisdiction
title: "Jackson County, OR"
classification: county
fips: "41029"
state: "OR"
demographics:
  population: 222645
  population_under_18: 45192
  population_18_64: 125113
  population_65_plus: 52340
  median_household_income: 73999
  poverty_rate: 12.36
  homeownership_rate: 65.95
  unemployment_rate: 5.36
  median_home_value: 430200
  gini_index: 0.4614
  vacancy_rate: 6.08
  race_white: 180152
  race_black: 1419
  race_asian: 2411
  race_native: 1369
  hispanic: 32570
  bachelors_plus: 70622
districts:
  - to: "us/states/or/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/or/districts/senate/28"
    rel: in-district
    area_weight: 0.4682
  - to: "us/states/or/districts/senate/3"
    rel: in-district
    area_weight: 0.3441
  - to: "us/states/or/districts/senate/2"
    rel: in-district
    area_weight: 0.1877
  - to: "us/states/or/districts/house/56"
    rel: in-district
    area_weight: 0.4682
  - to: "us/states/or/districts/house/5"
    rel: in-district
    area_weight: 0.3355
  - to: "us/states/or/districts/house/4"
    rel: in-district
    area_weight: 0.1877
  - to: "us/states/or/districts/house/6"
    rel: in-district
    area_weight: 0.0085
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Jackson County, OR

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 222645 |
| Under 18 | 45192 |
| 18–64 | 125113 |
| 65+ | 52340 |
| Median household income | 73999 |
| Poverty rate | 12.36 |
| Homeownership rate | 65.95 |
| Unemployment rate | 5.36 |
| Median home value | 430200 |
| Gini index | 0.4614 |
| Vacancy rate | 6.08 |
| White | 180152 |
| Black | 1419 |
| Asian | 2411 |
| Native | 1369 |
| Hispanic/Latino | 32570 |
| Bachelor's or higher | 70622 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 100% (congressional)
- [OR Senate District 28](/us/states/or/districts/senate/28.md) — 47% (state senate)
- [OR Senate District 3](/us/states/or/districts/senate/3.md) — 34% (state senate)
- [OR Senate District 2](/us/states/or/districts/senate/2.md) — 19% (state senate)
- [OR House District 56](/us/states/or/districts/house/56.md) — 47% (state house)
- [OR House District 5](/us/states/or/districts/house/5.md) — 34% (state house)
- [OR House District 4](/us/states/or/districts/house/4.md) — 19% (state house)
- [OR House District 6](/us/states/or/districts/house/6.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
