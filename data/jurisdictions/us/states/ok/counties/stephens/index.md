---
type: Jurisdiction
title: "Stephens County, OK"
classification: county
fips: "40137"
state: "OK"
demographics:
  population: 43551
  population_under_18: 9912
  population_18_64: 24597
  population_65_plus: 9042
  median_household_income: 61620
  poverty_rate: 18.02
  homeownership_rate: 74.39
  unemployment_rate: 5.23
  median_home_value: 145300
  gini_index: 0.4768
  vacancy_rate: 13.56
  race_white: 34862
  race_black: 644
  race_asian: 255
  race_native: 1434
  hispanic: 3783
  bachelors_plus: 8410
districts:
  - to: "us/states/ok/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/31"
    rel: in-district
    area_weight: 0.799
  - to: "us/states/ok/districts/senate/43"
    rel: in-district
    area_weight: 0.2009
  - to: "us/states/ok/districts/house/50"
    rel: in-district
    area_weight: 0.6686
  - to: "us/states/ok/districts/house/51"
    rel: in-district
    area_weight: 0.3313
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Stephens County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43551 |
| Under 18 | 9912 |
| 18–64 | 24597 |
| 65+ | 9042 |
| Median household income | 61620 |
| Poverty rate | 18.02 |
| Homeownership rate | 74.39 |
| Unemployment rate | 5.23 |
| Median home value | 145300 |
| Gini index | 0.4768 |
| Vacancy rate | 13.56 |
| White | 34862 |
| Black | 644 |
| Asian | 255 |
| Native | 1434 |
| Hispanic/Latino | 3783 |
| Bachelor's or higher | 8410 |

## Districts

- [OK-04](/us/states/ok/districts/04.md) — 100% (congressional)
- [OK Senate District 31](/us/states/ok/districts/senate/31.md) — 80% (state senate)
- [OK Senate District 43](/us/states/ok/districts/senate/43.md) — 20% (state senate)
- [OK House District 50](/us/states/ok/districts/house/50.md) — 67% (state house)
- [OK House District 51](/us/states/ok/districts/house/51.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
